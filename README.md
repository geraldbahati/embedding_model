# Embedding Model with OpenAI Support

This repository contains a versatile embedding model that's designed to work seamlessly with OpenAI and other large language models (LLMs). It offers an easy-to-use interface and can be integrated with other systems like `ZoteroDB` to fetch and process documents.

## Output Exmaple
**Question:**
What is The Meaning of Modularity?

Answer given with reference

**Response**
Modularity refers to the property of a system that has been decomposed into a set of cohesive and loosely coupled modules. These modules are the elementary and indivisible units of the system that can be reused across applications. Modularity allows for the system to be divided into smaller parts that can be refined independently, addressing the inherent complexity of the system. It is important in both complex systems, such as the Space Shuttle and personal computers, and in software design. Modularity in software design involves decomposing the system into smaller parts that can be refined independently, using approaches such as algorithmic decomposition and object-oriented decomposition. (Booch_Objectorientedanalysisand_20080831_7G95NMRG pages 81-82)

References

1. (Booch_Objectorientedanalysisand_20080831_7G95NMRG pages 81-82): Booch, Grady, Ivar Jacobson, and James Rumbaugh. Object-Oriented Analysis and Design with Applications. Third Edition. The Addison-Wesley Object Technology Series. 2023.


## Features

- **Easy Integration**: With just a few lines of code, you can integrate it with OpenAI or other LLMs.
- **ZoteroDB Support**: Fetch documents from Zotero and process them with ease.
- **Versatility**: Though optimized for OpenAI, you can use any other LLM of your choice.

### Usage

Make sure you have set your OPENAI_API_KEY environment variable.

Using the embedding model with OpenAI support is straightforward. To use unbowed_ai, you need to have a list of paths (valid extensions include: `.pdf`, `.txt`) and a list of citations (strings) that correspond to the paths. You can then use the `Docs` class to add the documents and then query them. Here's how you can set it up and run it:

#### 1. **Setup**

#### Initialization

Start by initializing the main components - `Docs` for managing your document embeddings:

```python
"""
Ensure you have set your OPENAI_API_KEY environment variable

from dotenv import load_dotenv

load_dotenv()

my_docs = [...] a list of paths to your documents(.pdf, .txt)
"""

from unbowed_ai import Docs

docs = Docs()
for d in my_docs:
    docs.add(d)

answer = docs.query("What is The Meaning of Modularity?")
print(answer.formatted_answer)
```

##### Output

**Modularity** refers to the property of a system that has been decomposed into a set of cohesive and loosely coupled modules. These modules are the elementary and indivisible units of software that can be reused across applications. Modularity allows for the organization of classes and objects into separate modules, which can be developed and refined independently. It also affects the locality of reference and the paging behavior of a virtual memory system. Modularity decisions can be influenced by various factors such as work assignments, subcontractor relationships, documentation and configuration management, and security considerations.

**Source**:
(Booch_Objectorientedanalysisand_20080831_7G95NMRG pages 81-82)

### References

1. Booch, Grady, Ivar Jacobson, and James Rumbaugh. *Object-Oriented Analysis and Design with Applications*. Third Edition. The Addison-Wesley Object Technology Series. 2023.

### CSV Support (New feature)

It is not that sophisticated can only support csv of specific form. It more specialized for timetable

#### Example

**Question** what do I have on Wednesday?

**Response from Unbowed AI**
On Wednesday, you have the following units scheduled:

- From 7-9am: SCO 211 in LT2.
- From 11-1pm: SCO 217 in AZ41. (Timetable2023 - Timetable Part 1)

References

(Timetable2023 - Timetable Part 1): "Timetable for Kenyatta University, Computer Science Course for 3rd year 1st Semester." Kenyatta University, 2023.


## Support for Zotero

The model can directly add file from the User's Zotero library depending on the query.

ake sure you have set your ZOTERO_API_KEY and ZOTERO_USER_ID environment variables.

```python
from unbowed_ai import Docs
from unbowed_ai.contrib import ZoteroDB


docs = Docs()
zotero = ZoteroDB(library_type="user")

for item in zotero.iterate(
    q="Further Programming Techniques",
    qmode="everything",
    sort="date",
    direction="desc",
    limit=100,
):
    print("Adding", item.title)
    docs.add(item.pdf, docname=item.key)
```

This adds maximum of 100 files to `Docs` class relating to **Further Programming Techniques**, the query passed as an argument.


## Extensive Example of this Model in Use

I'm using `streamlit` library. This module provides the tools needed to create a web-based interactive application.

The code sets up a Streamlit application where a user can query information from various documents (fetched from ZoteroDB and locally from a CSV). When a user poses a question, the system searches the documents for a relevant answer and displays it on the web interface.

```python
import streamlit as st
from dotenv import load_dotenv
from unbowed_ai import Docs
from unbowed_ai.contrib import ZoteroDB
from html_template import bot_template, css, user_template

# Load environment variables
load_dotenv()

def initialize_docs():
    """Initialize and populate the documents from ZoteroDB and local CSV."""

    # Initialize the Docs and ZoteroDB instances
    st.session_state.docs = Docs()
    st.session_state.zotero = ZoteroDB(library_type="user")

    # Add PDFs from ZoteroDB
    for item in st.session_state.zotero.iterate(
        q="Introduction to C++ Programming",
        qmode="everything",
        sort="date",
        direction="desc",
        limit=100,
    ):
        print("Adding", item.title)
        st.session_state.docs.add(item.pdf, docname=item.key)

    # Add local timetable CSV
    st.session_state.docs.add("timetable.csv")
    print("timetable.csv added")

def handle_user_input(user_input):
    """Handle the user's question and display the answer."""

    # Query the documents for the answer
    answer = st.session_state.docs.query(user_input)

    if answer:
        # Display the question and answer if found
        st.write(
            user_template.replace("{{MSG}}", answer.question),
            unsafe_allow_html=True,
        )
        st.write(
            bot_template.replace("{{MSG}}", answer.formatted_answer), unsafe_allow_html=True
        )
    else:
        # Inform the user if the answer is not found
        st.write(user_template.format(user_input))
        st.write(bot_template.format("Sorry, I don't know the answer to that."))

def main():
    """Main function to set up the Streamlit UI and handle interactions."""

    # Configure Streamlit page settings
    st.set_page_config(
        page_title="Chat with multiple PDFs", page_icon=":shark:", layout="wide"
    )

    # Add custom CSS
    st.write(css, unsafe_allow_html=True)

    # Initialize the Docs and ZoteroDB instances if not in session state
    if "zotero" not in st.session_state:
        st.session_state.zotero = None

    if "docs" not in st.session_state:
        initialize_docs()

    # UI Components
    st.title("Chat with multiple PDFs")
    st.header("Chat with multiple PDFs")
    user_question = st.text_input("Ask a question about your documents")

    # Handle the user's question if provided
    if user_question:
        handle_user_input(user_question)

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
```

That's it 😁

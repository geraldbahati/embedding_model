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
"""

from unbowed_ai import Docs

docs = Docs()
for d in my_docs:
    docs.add(d)

answer = docs.query("What is The Meaning of Modularity?")
print(answer.formatted_answer)
```
That's it 😑.

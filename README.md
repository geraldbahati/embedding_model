# Embedding Model with OpenAI Support

This repository contains a versatile embedding model that's designed to work seamlessly with OpenAI and other large language models (LLMs). It offers an easy-to-use interface and can be integrated with other systems like `ZoteroDB` to fetch and process documents.

## Features

- **Easy Integration**: With just a few lines of code, you can integrate it with OpenAI or other LLMs.
- **ZoteroDB Support**: Fetch documents from Zotero and process them with ease.
- **Versatility**: Though optimized for OpenAI, you can use any other LLM of your choice.

### Usage

Using the embedding model with OpenAI support is straightforward. Here's how you can set it up and run it:

#### 1. **Setup**

Before using the provided code, ensure you've installed the necessary libraries.

```bash
pip install unbowed_ai
```

#### Initialization

Start by initializing the main components - `Docs` for managing your document embeddings and `ZoteroDB` to interact with Zotero:

```python
from unbowed_ai import Docs  # noqa: E402
from unbowed_ai.contrib import ZoteroDB  # noqa: E402

docs = Docs()
zotero = ZoteroDB(library_type="user")  # Use "group" for group library
```

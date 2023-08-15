from setuptools import setup

# for typing
__version__ = ""
exec(open("unbowed_ai/version.py").read())

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="unbowed-ai",
    version=__version__,
    description="LLM Chain for answering questions from docs ",
    author="Gerald Bahati",
    author_email="bahatigerald0@gmail.com",
    url="https://github.com/geraldbahati/multiple-pdf-chat",
    license="Apache License 2.0",
    packages=["unbowed_ai", "unbowed_ai.contrib"],
    install_requires=[
        "pypdf",
        "langchain>=0.0.198",
        "openai >= 0.27.8",
        "faiss-cpu",
        "PyCryptodome",
        "html2text",
        "tiktoken>=0.4.0",
    ],
    test_suite="tests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)

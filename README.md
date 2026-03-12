# LangChain Chains Examples (LangChain 1.x)

This repository contains examples of different types of chains in LangChain using the modern LangChain 1.x API.
The project demonstrates simple, sequential, parallel, and conditional chains using LCEL (LangChain Expression Language).

All examples use:

* LangChain 1.x
* langchain_core
* langchain_openai
* Runnable API
* PromptTemplate
* Output Parsers
* Graph visualization

---

## Requirements

Install dependencies:

pip install langchain langchain-core langchain-openai python-dotenv

Create a .env file:

OPENAI_API_KEY=your_api_key_here

---

## Files Included

### simplechain.py

Demonstrates a basic chain.

Uses:

* PromptTemplate
* ChatOpenAI
* StrOutputParser

Chain structure:

prompt | model | parser

Features:

* Simple execution
* Chain visualization

---

### sequentialchain.py

Demonstrates sequential chaining.

Flow:

topic → report → summary

Chain:

template1 | model | parser | template2 | model | parser

Features:

* Multi-step processing
* Output passed to next step
* Graph visualization

---

### parallelchain.py

Demonstrates parallel execution using RunnableParallel.

Flow:

text → notes + quiz → merge

Steps:

1. Generate notes
2. Generate quiz
3. Merge both

Uses:

* RunnableParallel
* Multiple prompts
* Merge chain

Features:

* Parallel execution
* Multiple outputs
* Combined result

---

### conditionalchain.py

Demonstrates conditional branching using RunnableBranch.

Flow:

feedback → sentiment classifier → branch → response

Steps:

1. Detect sentiment
2. Route to correct prompt
3. Generate response

Uses:

* RunnableBranch
* RunnableLambda
* PydanticOutputParser

Features:

* Conditional chains
* Structured output
* Branching logic

---

## Technologies Used

* LangChain 1.x
* langchain_core
* langchain_openai
* Runnable API
* Pydantic
* PromptTemplate
* Output Parsers

---

## Important Note

This repo uses modern LangChain syntax.

Older tutorials may use:

langchain.chains
langchain.schema
langchain.output_parsers

These are outdated.

New imports use:

langchain_core
langchain_openai
langchain_core.runnables

---

## Graph Visualization

Each chain prints its structure using:

chain.get_graph().print_ascii()

Example:

PromptTemplate
|
ChatOpenAI
|
StrOutputParser

---

## Chains Covered

Simple chain → simplechain.py


Sequential chain → sequentialchain.py


Parallel chain → parallelchain.py


Conditional chain → conditionalchain.py

---

## Purpose

This repo demonstrates:

* LCEL syntax
* Runnable API
* Sequential chains
* Parallel chains
* Conditional chains
* Structured outputs

and how modern LangChain works internally.

---

## Author

Irfan Mohammed

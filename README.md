# RAG LangChain Project

This repository contains the code for implementing a **Retrieval-Augmented Generation (RAG)** system using **LangChain**.

## Description

The project demonstrates how to build and deploy a RAG system, which integrates large language models (LLMs) with external data sources to improve the quality and accuracy of generated text. It uses **LangChain**, an open-source framework that simplifies the integration of LLMs with various data sources and retrieval systems.

## Features

- **RAG-based architecture**: Combine pre-trained models with document retrieval for more context-aware responses.
- **LangChain integration**: Utilize LangChain for building RAG pipelines with ease.
- **Customizable**: Easily extend the system to work with different document types and retrieval methods.
- **Multilingual support**: Capable of working with multiple languages depending on the used model.


### Installation
## Clone the repository:
```bash
git clone https://github.com/tienhuynh96/rag_langchain.git
cd rag_langchain
```
## Create a virtual environment:
``` bash
conda  create -n rag_env
conda activate rag_env
```
## Install the dependencies:
``` bash
pip install -r requirements.txt
```

## Usage
# Prepare your documents:
Place your PDF files in a designated directory: generative_ai and machine_learning.

# Run the application:
```bash
uvicorn app:app --host=127.0.0.1 --port=5000 --reload
```

## Access the API:

Navigate to http://127.0.0.1:5000/ in your browser or use tools like curl or Postman to interact with the API endpoints.

## Features
`Document Ingestion`: Supports loading and processing of PDF documents.

`Text Splitting`: Utilizes customizable chunk sizes and overlaps for text segmentation.

`Embedding Generation`: Generates embeddings using Sentence Transformers.

`Retrieval Mechanism`: Implements FAISS for efficient similarity search.

`Language Models`: Integrates with Hugging Face models for response generation.

`API Interface`: Provides a FastAPI-based interface for user interaction.

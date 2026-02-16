# Simple RAG Project using Google Gemini
This repository contains a small Retrieval-Augmented Generation (RAG) application built using Google Gemini. 
It is designed to evaluate understanding of end-to-end RAG architecture. 
The application ingests local text documents, indexes them using a vector database, and retrieves the most relevant document chunks to pass to Google Gemini to generate an answer.

## 🛠️ Tech Stack
* **Backend:** Python with FastAPI 
* **Frontend:** Streamlit 
* **LLM & Embeddings:** Google Gemini API (`gemini-2.5-flash` and `gemini-embedding-001`) 
* **Vector Database:** ChromaDB

## 📋 Prerequisites
1. Python 3.11.9 installed.
2. A Google Gemini API Key.

## 🚀 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/amantyagi09/RAG-Assignment.git
   cd <your-project-folder>
   
2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   
3. **Environment Setup:**  
   Create a .env file in the root directory and add your API key.
   
5. **Data Preparation:**  
   You can use either the same data given in data folder or can change the information in the .txt files as of your choice.

## 💻 Usage

1. **Document Ingestion**
   </br>
   Run the basic document loader to chunk, embed, and store your text files:
   
   ```bash
   python ingest.py

3. **Run the Application**  
   Start the Streamlit UI to interact with your documents:
    
   ```bash
   streamlit run app.py
   ```
   The application will display a clean final answer based on your query and include explicit source citations (e.g., "Source: doc3.txt").


## 📝 Design Notes  
This architecture utilizes a straightforward end-to-end RAG pipeline. I chose Chroma as the local vector database for seamless vector indexing and search without requiring external cloud infrastructure. Google Gemini handles both the embeddings and the LLM response generation. The query pipeline retrieves the top contextual chunks, constructs a strict prompt using only that retrieved context, and returns the generated answer alongside clear source citations. To fulfill the optional bonuses, I implemented a simple UI using Streamlit, wrapped alongside a FastAPI backend to demonstrate a scalable approach.

   
   

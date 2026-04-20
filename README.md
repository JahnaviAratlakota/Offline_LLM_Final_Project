# README.md

# Offline LLM Chatbot with Semantic Similarity Analysis

## 📌 Project Overview

This project is an offline AI chatbot that uses a local Large Language Model (LLM) to generate responses without internet access. It also evaluates answer relevance using SBERT semantic similarity and stores chat history locally in JSON format.

## 🚀 Features

* Offline chatbot using local LLM
* Streamlit user interface
* Chat history storage
* Search previous chats
* Semantic similarity score using SBERT
* Secure local processing

## 🛠 Technologies Used

* Python
* Streamlit
* LM Studio
* Qwen (Local LLM)
* Sentence Transformers (SBERT)
* Scikit-learn
* JSON

## 🏗 Architecture Flow

User Input
→ Streamlit UI
→ Local LLM (LM Studio)
→ Generate Response
→ SBERT Similarity Check
→ Display Result
→ Save Chat History (JSON)

## ▶️ How to Run

1. Install dependencies:

pip install -r requirements.txt

2. Run Streamlit app:

streamlit run app.py

3. Ensure LM Studio is running with your local model.

## 📂 Project Structure

app.py
requirements.txt
utils.py
sample.py
score.py
agents/
chats/

## 🔐 Advantages

* No internet required
* Better privacy
* Fast response
* Easy to use

## 🔮 Future Enhancements

* Voice input
* Multilingual support
* Document question answering
* Better memory system

## 👨‍💻 Author

Jahnavi

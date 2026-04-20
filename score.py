# ================================
# SBERT Cosine Similarity Example
# ================================

import re
import nltk
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK resources (run once)
nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# -------------------------------
# 1️⃣ Input Question & Answer
# -------------------------------

question = "What is python and tell me road map for learning python?"

answer = """
Python is a high-level, versatile programming language widely used in web development,
data science, machine learning, automation, and AI. A roadmap includes learning basics,
data structures, OOP, file handling, projects, and advanced topics like ML and web frameworks.
"""

# -------------------------------
# 2️⃣ Text Cleaning Function
# -------------------------------

def clean_text(text):
    text = text.lower()                              # lowercase
    text = re.sub(r'[^a-z\s]', '', text)             # remove special chars
    tokens = word_tokenize(text)                     # tokenization
    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if w not in stop_words]  # remove stopwords
    return " ".join(tokens)

clean_question = clean_text(question)
clean_answer = clean_text(answer)

print("Clean Question:", clean_question)
print("Clean Answer:", clean_answer)

# -------------------------------
# 3️⃣ Load SBERT Model
# -------------------------------

model = SentenceTransformer('all-MiniLM-L6-v2')

# -------------------------------
# 4️⃣ Vectorization (Embeddings)
# -------------------------------

embeddings = model.encode([question, answer])

question_vector = embeddings[0].reshape(1, -1)
answer_vector = embeddings[1].reshape(1, -1)

# -------------------------------
# 5️⃣ Cosine Similarity
# -------------------------------

similarity_score = cosine_similarity(question_vector, answer_vector)[0][0]

print("\nCosine Similarity Score:", round(similarity_score, 4))
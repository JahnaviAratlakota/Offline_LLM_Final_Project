import streamlit as st
import time

from agents.llm_agent import llm_agent
from agents.sbert_agent import sbert_agent
from utils import save_chat, list_chats, generate_chat_name

# -------------------------------
# Session State
# -------------------------------
if "chat_id" not in st.session_state:
    st.session_state.chat_id = None

if "chat_name" not in st.session_state:
    st.session_state.chat_name = ""

if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("⚛ AI Chatbot")

if st.sidebar.button("➕ New Chat"):
    st.session_state.chat_id = f"chat_{int(time.time())}"
    st.session_state.chat_name = "New Chat"
    st.session_state.messages = []

search_query = st.sidebar.text_input("🔍 Search chats")

st.sidebar.markdown("### 💾 Chat History")
for chat in list_chats():
    if search_query.lower() in chat["chat_name"].lower():
        if st.sidebar.button(chat["chat_name"], key=chat["chat_id"]):
            st.session_state.chat_id = chat["chat_id"]
            st.session_state.chat_name = chat["chat_name"]
            st.session_state.messages = chat["messages"]

# -------------------------------
# Main UI
# -------------------------------
st.title("֎ Offline LLMs ")
st.caption("Enabling Secure, Real-Time Human-AI Conversations Without Internet Using On-Device Language Models")

if st.session_state.chat_name:
    st.subheader(st.session_state.chat_name)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type your message...")

# -------------------------------
# Chat Logic
# -------------------------------
if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    if st.session_state.chat_name == "New Chat":
        st.session_state.chat_name = generate_chat_name(user_input)

    with st.spinner("🤖 Please wait..."):
        bot_response = llm_agent(st.session_state.messages)

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_response}
    )

    with st.chat_message("assistant"):
        st.markdown(bot_response)

        analysis = sbert_agent(user_input, bot_response)
        #if user input is hii hello then skip semantic analysis
        if not user_input.lower() in ["hi", "hello", "hey", "hi!", "hello!", "hey!", "good morning", "good afternoon", "good evening","bye","goodbye","thank you","thanks",'hii']:
            with st.expander("🔍 Analysis"):
                st.write("**Clean Question:**", analysis["clean_question"])
                st.write("**Clean Answer:**", analysis["clean_answer"])
                st.success(f"Similarity Score: **{analysis['similarity']}**")

    if st.session_state.chat_id:
        save_chat(
            st.session_state.chat_id,
            st.session_state.chat_name,
            st.session_state.messages
        )

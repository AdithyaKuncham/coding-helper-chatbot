import streamlit as st
from ui import apply_styles, sidebar, display_chat
from llm_client import get_llm_response

# Page config
st.set_page_config(page_title="Coding Helper Chatbot", layout="wide")

apply_styles()

# Initialize session
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
sidebar()

# Main UI
st.title("💻 Coding Helper Chatbot")
st.markdown("*Ask coding questions, debug code, and learn programming concepts.*")
st.divider()

# Chat display
display_chat()

# Input area
col1, col2 = st.columns([6, 1])

with col1:
    user_input = st.text_input("Type your coding question...", key="user_input", label_visibility="collapsed")

with col2:
    send_button = st.button("Send", use_container_width=True)

# Handle message
if send_button and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Thinking..."):
        try:
            reply = get_llm_response(user_input)
            st.session_state.messages.append({"role": "assistant", "content": reply})

        except Exception as e:
            st.error(f"Error: {str(e)}")

    st.rerun()
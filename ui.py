import streamlit as st

def apply_styles():
    st.markdown("""
    <style>
        .stApp { background-color: #0e1117; }
        .user-message {
            background-color: #2b5278;
            padding: 10px 15px;
            border-radius: 15px;
            margin: 5px 0;
            text-align: right;
            margin-left: 20%;
        }
        .bot-message {
            background-color: #1e2530;
            padding: 10px 15px;
            border-radius: 15px;
            margin: 5px 0;
            text-align: left;
            margin-right: 20%;
        }
    </style>
    """, unsafe_allow_html=True)


def sidebar():
    with st.sidebar:
        st.title("💡 Example Questions")

        examples = [
            "Explain binary search in Java",
            "Write a Python program for factorial",
            "Explain sliding window technique",
            "Show quicksort implementation"
        ]

        for example in examples:
            if st.button(example):
                st.session_state.messages.append({"role": "user", "content": example})
                st.rerun()

        st.divider()

        if st.button("🗑️ Clear Chat"):
            st.session_state.messages = []
            st.rerun()


def display_chat():
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-message">{message["content"]}</div>', unsafe_allow_html=True)
import streamlit as st
from chat import ask_question,history


# st.title("My Personal Chatbot")
st.markdown(
    "<h1 style='text-align:center; color:#2196F3;'>My Personal Chatbot</h1>",
    unsafe_allow_html=True
)

# Input box to ask question
st.markdown(
    "<h4 style='text-align:left; color:#2196F3;'>Let's Chat</h4>",
    unsafe_allow_html=True
)
question = st.text_input("Ask something:")

# Ask button functionality
if st.button("Ask", type = "primary"):
    if question.strip():
        placeholder = st.empty()
        response_text = ""

        for word in ask_question(question):
            response_text += word
            placeholder.markdown(f"**Assistant:** {response_text}")

# Conversation section
st.markdown(
    "<h4 style='text-align:left; color:#2196F3;'>Conversation History</h4>",
    unsafe_allow_html=True
)
# Write write
for item in history:
    st.write(item)

# Clear Chat
if st.button("Clear Chat", type ="primary"):
    history.clear()

































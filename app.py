import streamlit as st
from chat import ask_question,history


# st.title("My Personal Chatbot")
st.markdown(
    "<h1 style='text-align:center; color:#2196F3;'>My Personal Chatbot</h1>",
    unsafe_allow_html=True
)

# Input box to ask question
question = st.text_input("Ask something:")
# Button to ask question
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("Ask", type = "primary"):
        if question.strip():
            placeholder = st.empty()
            response_text = ""

            for word in ask_question(question):
                response_text += word
                placeholder.markdown(f"**Assistant:** {response_text}")

# Conversation section
st.subheader("Conversation")
for item in history:
    st.write(item)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Clear Chat", type ="primary"):
        history.clear()

































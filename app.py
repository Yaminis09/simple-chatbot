import streamlit as st
from chat import ask_question,history


st.title("My Personal Chatbot")
# Input box to ask question
question = st.text_input("Ask something:")

# if st.button("Ask"):
#     if question.strip():
#         answer = ask_question(question)
#         st.write("**Assistant:**", answer)


st.subheader("Conversation")
for item in history:
    st.write(item)

if st.button("Clear Chat"):
    history.clear()

































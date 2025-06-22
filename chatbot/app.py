from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY", "")

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that answers user's questions."),
        ("user", "Question: {question}"),
    ]
)

# Streamlit UI
st.title("Chatbot using Llama3.2 with Ollama")

input_text = st.text_input("Ask me anything:")


# Set up the LLM using Ollama
llm = ChatOllama(model="llama3.2:latest")

# Chain
chain = prompt | llm | StrOutputParser()

# Output
if input_text:
    st.write(chain.invoke({"question": input_text}))

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM
# from langchain_community import Ollama  #we cannot use this as third party things ar enow separated in langchain_community package and we have to install it separately, but we can use ollama llm from langchain_ollama package which is working fine.

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

#os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")  #for openai api llm

#langsmith tracking:for monitoring and debugging the chain execution
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_PROJECT"] = "TestProject"

#prompt template:
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant.Please response to the user queries."),
        ("user", "Question:{question}"),
    ]
)

#streamlit framework:
st.title("Langchain Streamlit App")
input_text = st.text_input("Enter your question here:")

#openai llm:
#llm = ChatOpenAI(model="gpt-3.5-turbo")   #paid llm
llm=OllamaLLM(model="llama2")   #local llm using ollama
output_parser = StrOutputParser()  #output shown using this
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))
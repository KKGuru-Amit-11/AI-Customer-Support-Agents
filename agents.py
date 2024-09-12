# Import Reqiured Library
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import os
import streamlit as st
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from tools import search_tool,scrape_tool

# LLM Monitering
os.environ['LANGCHAIN_API_KEY']=st.secrets['LANGSMITH_API_KEY']
os.environ['LANCHAIN_PROJECT']='Customer Support Moniter'
os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ['LANGCHAIN_ENDPOINT']="https://api.smith.langchain.com"


# # Creating LLM Model
# os.environ['GOOGLE_API_KEY']=st.secrets['GOOGLE_API_KEY']
# llm_model = ChatGoogleGenerativeAI(model='gemini-1.5-flash',
#                                    api_key=os.getenv('GOOGLE_API_KEY'))

# Creating LLM Model
os.environ['GROQ_API_KEY']=st.secrets['GROQ_API_KEY']
llm_model = ChatGroq(model='llama3-8b-8192',api_key=os.getenv('GROQ_API_KEY'))

# Creating Agent
support_agent = Agent(
    role='Senior Support Representative',
    goal='Be Most Friendly and Helpful',
    backstory='''you are working at analytix4T (https://analytx4t.com/) and you are 
    now working on providing support to {customer}, a super 
    important customer for your company you need to make sure that you 
    provide the best support for their inquiry. Make Sure to provide full 
    complete answers and make make no assumptions''',
    verbose=True,
    allow_delegation=False,
    tools = [search_tool,scrape_tool],
    llm=llm_model
)

support_quality_assurance_agent= Agent(
    role='Support Quality Assurance Specialist',
    goal='Get Recognition for Providing the best support Quality Assurance in your team',
    backstory='''You are work at analytix4t (https://analytx4t.com/) and you are wokring with your team on a request from {customer}. 
    ensuring that the support representative is providing the best support possible. 
    you need to make sure that the support representative is providing full 
    complete answers, and make no assumption''',
    verbose=True,
    allow_delegation=True,
    tools = [search_tool,scrape_tool],
    llm=llm_model
)

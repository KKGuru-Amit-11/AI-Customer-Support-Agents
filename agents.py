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

# Creating Header for web Page:
st.header('**Multi AI Agent Customer Support...**')

# LLM Monitering
os.environ['LANGCHAIN_API_KEY']=st.secrets['LANGSMITH_API_KEY']
os.environ['LANCHAIN_PROJECT']='Customer Support Moniter'
os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ['LANGCHAIN_ENDPOINT']="https://api.smith.langchain.com"

# Getting Task From Web
with st.form(key='Query',clear_on_submit=True):
    cus_name=st.text_input(label='**Enter Your Name:**')
    cus_inquiry=st.text_input(label='**Enter Your Inquiry:**')
    model_name=st.selectbox(label='**Select Model Name:**', options=["Gemini Model","Groq Model"],index=None)
    submit_button = st.form_submit_button('Submit.')
    if submit_button:
        st.info('Input Details...')
        st.markdown(f'Customer Name: {cus_name} ...')
        st.markdown(f'Inquiry: {cus_inquiry} ...')

# # Creating LLM Model
def model_selection(value):
    if value == 'Gemini Model':
        os.environ['GOOGLE_API_KEY']=st.secrets['GOOGLE_API_KEY']
        llm_model = ChatGoogleGenerativeAI(model='gemini-1.5-flash',api_key=os.getenv('GOOGLE_API_KEY'))
        return llm_model
    else:
        os.environ['GROQ_API_KEY']=st.secrets['GROQ_API_KEY']
        llm_model = ChatGroq(model='llama3-8b-8192',api_key=os.getenv('GROQ_API_KEY'))
        return llm_model

llm_model=model_selection(model_name)

# Creating Agent
support_agent = Agent(
    role='Senior Support Representative',
    goal='Be Most Friendly and Helpful',
    backstory='''you are working at techshiney (https://techshiney.com/) and you are 
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
    backstory='''You are work at techshiney (https://techshiney.com/) and you are wokring 
    with your team on a request from {customer}. ensuring that the support representative 
    is providing the best support possible. you need to make sure that the support 
    representative is providing full complete answers, and make no assumption''',
    verbose=True,
    allow_delegation=True,
    tools = [search_tool,scrape_tool],
    llm=llm_model
)

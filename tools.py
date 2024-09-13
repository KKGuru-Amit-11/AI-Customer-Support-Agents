# Import Require Library
import os
import streamlit as st
from crewai_tools import SerperDevTool,ScrapeWebsiteTool

os.environ['SERPER_API_KEY'] = st.secrets['SERPER_API_KEY']

search_tool=SerperDevTool()
scrape_tool=ScrapeWebsiteTool(website_url='https://techshiney.com/')

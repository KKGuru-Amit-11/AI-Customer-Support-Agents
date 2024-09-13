# Import Requred Library
import streamlit as st
from crewai import Crew,Process
from agents import support_agent,support_quality_assurance_agent,llm_model
from tasks import inquiry_resolution,quality_assurance_review

# Creating Header for web Page:
st.header('**Multi AI Agent Customer Support...**')

crew = Crew(
    agents=[support_agent,support_quality_assurance_agent],
    tasks=[inquiry_resolution,quality_assurance_review],
    manager_llm=llm_model,
    process=Process.sequential,
    verbose=True
)

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
        st.markdown(f'Model Name: {model_name} ...')

inputs={
    'customer':cus_name,
    'inquiry':cus_inquiry
}

if st.button("**Generate**..."):
    with st.spinner('Generating Response...'):
        result=crew.kickoff(inputs=inputs)
        res=str(result)
        st.info('Here is Response')
        st.markdown(result)
        st.download_button(label='Download Text File'
                           ,file_name=f'cus_{cus_name}_query_solution.txt',data=res)

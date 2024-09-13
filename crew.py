# Import Requred Library
import streamlit as st
from crewai import Crew,Process
from agents import support_agent,support_quality_assurance_agent,llm_model,cus_name,cus_inquiry
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

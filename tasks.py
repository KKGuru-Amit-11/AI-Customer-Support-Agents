# Import Required Library
from crewai import Task
from agents import support_agent,support_quality_assurance_agent

inquiry_resolution = Task(
    description='''{customer} just reached out with a super important inquiry ask: {inquiry}\n
    {customer} is the one that reached out. make sure to use everything 
    you know to provide the best support possile. you must strive to provide a complete 
    and accurate response to the customer's inquiry''',
    expected_output='''A detailed,informative response to the custome's inquiry that 
    addresses all aspects of their question. The response should include references 
    to everything external data or solutions ensure the answer is complete leaving no 
    questions unanswered, and maintain a helpful and friendly tone throughout''',
    agent=support_agent
)

quality_assurance_review = Task(
    description='''Review the response drafted by the Seniour Support Representation for 
    {customer} 's inquiry. Ensure that the answer is comprehensive,accurate, and adheres to 
    the high-quality standards expected for customer support. Verify that all parts of the 
    customer's inquiry have been addressed throughly with a helpful and friendly tone. check 
    for references and sources used to find the information, ensuring the response is well-support 
    and leaves no questions unanswered for their inquiry.''',
    expected_output='''A Final, detailed, and infomative response ready to  be send to the customer
    This response should fully addess the customer's inquiry, incorporating all relevant 
    feadback and  improvment. don't be too formal, we are a chill and cool company but 
    maintain a professional and friendly tone throughout''',
    agent=support_quality_assurance_agent
)
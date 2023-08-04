import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st


#Display the Page Title
Page_Title= st.markdown("<h1 style='text-align: center; font-size: 45px;'>Data Analyst Jobs - EDA Process</h1>", unsafe_allow_html=True)

#Display the Page Subtitle
st.markdown("<h1 style='text-align: center; font-size: 25px;'>EDA Process By Marwan Mohamed</h1>", unsafe_allow_html=True)
st.markdown('----')

# Load the image
image = st.image("Data Analysis.jpg")

#Display Introduction
st.markdown("<h1 style='text-align: Left; font-size: 25px;'>What is data analysis?</h1>", unsafe_allow_html=True)

#Disply Introduction Data
st.write("Data analysis is the process of gleaning insights from data to inform better business decisions.                                     The process of analyzing data typically moves through five iterative phases:")

st.write("- Identify the data you want to analyze")
st.write("- Collect the data")
st.write("- Clean the data in preparation for analysis")
st.write(" - Analyze the data")                 
st.write("- Interpret the results of the analysis")

#Video Formating
st.markdown("<h1 style='text-align: Left; font-size: 25px;'>Watch This Video!</h1>", unsafe_allow_html=True)

st.video("index.webm")



st.markdown("-----")

st.markdown("<h1 style='text-align: Left; font-size: 25px;'>Data analyst tasks and responsibilities</h1>", unsafe_allow_html=True)


st.write("A data analyst is a person whose job is to gather and interpret data in order to solve a specific problem. The role includes plenty of time spent with data but entails communicating findings too.")
st.write("- Gather data: Analysts often collect data themselves. This could include conducting surveys, tracking visitor characteristics on a company website, or buying datasets from data collection specialists.")
st.write("- Clean data: Raw data might contain duplicates, errors, or outliers. Cleaning the data means maintaining the quality of data in a spreadsheet or through a programming language so that your interpretations won’t be wrong or skewed. ")
st.write("- Model data: This entails creating and designing the structures of a database. You might choose what types of data to store and collect, establish how data categories are related to each other, and work through how the data actually appears.")
st.write("- Interpret data: Interpreting data will involve finding patterns or trends in data that could answer the question at hand.")
st.write(" - Present: Communicating the results of your findings will be a key part of your job. You do this by putting together visualizations like charts and graphs, writing reports, and presenting information to interested parties.")


st.markdown("-----")


st.markdown("<h1 style='text-align: Left; font-size: 25px;'>What tools do data analysts use?</h1>", unsafe_allow_html=True)

st.write(" - Microsoft Excel")
st.write(" - Google Sheets")
st.write(" - SQL")
st.write(" - Tableau")
st.write(" - R or Python")
st.write(" - SAS")
st.write(" - Microsoft Power BI")
st.write(" - Jupyter Notebooks")


st.markdown("------")

st.markdown("<h1 style='text-align: Left; font-size: 25px;'>Introduction About The Data Analyst Jobs EDA Process</h1>",unsafe_allow_html=True)

st.write("- The objective of the present study is to conduct an exploratory analysis of data related to the job title, job description, and salary estimate for Data Analyst positions.")
st.write("- The dataset under investigation contains over 2000 job listings for Data Analyst roles, including various features such as Salary Estimate, Location, Company Rating, and Job Description, among others.")
st.write("- Our mission is to conduct an analysis process to find out helpful insights such as the best jobs by salary and company rating, which skills are needed to be a qualified Data Analyst, and which languages & programs are essential for this job.")

st.markdown("------")

st.markdown("<h1 style='text-align: Left; font-size: 25px;'>Questions should be answered after running this analysis</h1>",unsafe_allow_html=True)

st.write(" - What is the minimum salary for a data analyst jobs in general?")
st.write(" - What is the maximum salary for a data analyst jobs in general?")
st.write(" - What is the average salary for a data analyst jobs in general?")
st.write(" - What is the minimum salary for a data analyst job title?")
st.write(" - What is the maximum salary for a data analyst job title? ")
st.write(" - What is the average salary for a data analyst job title?")
st.write(" - Which job title is needed the most?")
st.write(" - Which industry has the most job openings related to data analyst positions?")
st.write(" - Which sector has the most job openings related to data analyst positions?")
st.write(" - What are the required programming languages & Program Skills needed for each job title?")
st.write(" - What is the data analyst Jobs Salary Range based on Company Name with Rating Scores?")







# Define the questions and their corresponding chart types
questions = {
    "What is the minimum salary for a data analyst jobs in general?": "Chart_1",
    "What is the maximum salary for a data analyst jobs in general?": "Chart_2",
    "What is the average salary for a data analyst jobs in general?": "Chart_3",
    "What is the minimum salary for a data analyst job title?": "Chart_4",
    "What is the maximum salary for a data analyst job title?": "Chart_5",
    "What is the average salary for a data analyst job title?": "Chart_6",
    "Which job title is needed the most?": "Chart_7",
    "Which industry has the most job openings related to data analyst positions?": "Chart_8",
    "Which sector has the most job openings related to data analyst positions?": "Chart_9",
    "What are the required programming languages & Program Skills needed for each job title?": "Chart_10",
    "What is the data analyst Jobs Salary Range based on Company Name with Rating Scores?": "Chart_11"
}

st.markdown("-----")



# Display the dropdown list
st.write("<h3 style='font-weight: bold;'>Select Yor Question:</h2>", unsafe_allow_html=True)
question = st.selectbox("", list(questions.keys()))

# Display the chart based on the selected question
if question == "What is the minimum salary for a data analyst jobs in general?":
    st.image("Chart_1.png")
    st.write("- Findings: Minimum salary for data analyst is an average between 40-70K, but we have quite skewed distribution on the minimum salary.")
    
elif question == "What is the maximum salary for a data analyst jobs in general?":
    st.image("Chart_2.png")
    st.write("- Findings: Maximum salary for data analyst is an average between 65-90K, but we have quite skewed distribution on the maximum salary.")
    
elif question == "What is the average salary for a data analyst jobs in general?":
    st.image("Chart_3.png")
    st.write("- Findings: Average salary for data analyst is an average between 60-80K, but we have skewed distribution on the average salary.")
    
elif question == "What is the minimum salary for a data analyst job title?":
    st.image("Chart_4.png")
    st.write("- Findings: Minimum salary for data analyst is an average between 40-60K, but we have quite skewed distribution on the minimum salary.")
    
elif question == "What is the maximum salary for a data analyst job title?":
    st.image("Chart_5.png")
    st.write("- Findings: Maximum salary for data analyst is an average between 67-95K, but we have quite skewed distribution on the maximum salary.")
    
elif question == "What is the average salary for a data analyst job title?":
    st.image("Chart_6.png")
    st.write("- Findings: Average salary for data analyst is an average between 55-80K, but we have skewed distribution on the average salary.")
    
elif question == "Which job title is needed the most?":
    st.image("Chart_7.png")
    st.markdown("<h1 style='text-align: Left; font-size: 20px;'>Findings:</h1>",unsafe_allow_html=True)
    st.write("- Data Analyst")
    st.write("- Senior Data Analyst")
    st.write("- Junior Data Analyst")
    st.write("- Business Data Analyst are the most used titles in the job advertisements")
    
    
elif question == "Which industry has the most job openings related to data analyst positions?":
    st.image("Chart_8.png")
    st.markdown("<h1 style='text-align: Left; font-size: 20px;'>Findings:</h1>",unsafe_allow_html=True)
    st.write("- IT Services")
    st.write("- Staffing & Outsourcing")
    st.write("- Consulting")
    st.write("- Computer Hardware & Software are the most data analyst job opening advertised industries.")
    st.write("- It is important to mention also, Banking (Investment Banks - Banks) also advertised 129 (combined) data analyst job openings")
    

elif question == "Which sector has the most job openings related to data analyst positions?":
    st.image("Chart_9.png")
    st.markdown("<h1 style='text-align: Left; font-size: 20px;'>Findings:</h1>",unsafe_allow_html=True)
    st.write("- Information Technology")
    st.write("- Business Services")
    st.write("- Finance")
    st.write("- Health Care are the most data analyst job opening advertised sectors.")
    
    
elif question == "What are the required programming languages & Program Skills needed for each job title?":
    st.image("Chart_10.png")
    st.write("- Findings: As we can see from the above table, SQl is required the most among other languages & programs than Excel and Python, Tableau is the least one.")
     

elif question == "What is the data analyst Jobs Salary Range based on Company Name with Rating Scores?":
    st.image("Chart_11.png")
    st.write("- Findings: Minimum salary 110K is OK, I mean quite OK for working 3.9 rating company, like Netflix")
    st.image("Chart_12.png")
    st.write("- Findings: Maximum Salary of 190K offered by companies like Diverse Lynx & Conor Group")
    st.image("Chart_13.png")
    st.write(" - Findings: Best Average Salary of 150K offered by companies like Diverse Lynx, Conor Group & ICONMA ")
    
    
    
    
st.markdown("-----")

#Conclusion Data

st.markdown("<h1 style='text-align: Left; font-size: 30px;'>Conclusion:</h1>", unsafe_allow_html=True)    
st.write("- Regarding the salaries of Data analysts, we can figure out that the maximum salary is average between 65K-95K, the minimum salary is average between 40K-60K, and finally the average salary is an average between 55K-80K.")

st.write("- Coming to job titles, Data Analyst, Senior Data Analyst, Junior Data Analyst, and Business Data Analyst are the most used titles in job advertisements.")    

st.write("- IT Services, Staffing & Outsourcing, Health Care Services & Hospitals, Consulting, Computer Hardware & Software are the most data analyst job openings advertised industries.") 

st.write("- Information Technology, Business Services, Finance, and Health Care are the most data analyst job openings advertised sectors.") 

st.write("- SQL is required the most for data analyst job openings among other languages & programs than Excel and Python, Tableau is the least one.") 

st.write("- Highly rated companies offer a minimum salary of 110K, an average salary of 150K, and a maximum salary of 190K.") 

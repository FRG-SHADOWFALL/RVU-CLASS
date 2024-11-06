# Import necessary libraries
import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd

# --- Title and Introduction ---
st.title("RVU Visualization Workshop")
st.write("### Author: Siddharth Ravishankar")
st.write("#Section-F")
st.subheader("Interactive Visualizations with Plotly and Streamlit")

# --- Input for Author Information ---
st.sidebar.header("Visualization Skill Workshop - Plotly")
name = st.sidebar.text_input("Enter your name")
usn = st.sidebar.text_input("Enter your roll number")
instructor_name = st.sidebar.text_input("Course Instructor Name")

# --- Load Dataset ---
tips = sns.load_dataset('tips')  # Loading the tips dataset

# Display the first few rows of the dataset
st.write("## Dataset Overview")
st.write(tips.head())

# --- Task 2: Interactive Bar Chart ---
st.subheader("Task 2: Bar Chart - Average Tip by Day")
# Bar Chart: Average Tip by Day with color for each day
fig2 = px.bar(
    tips, x='day', y='tip', color='day',
    title='Average Tip by Day',
    labels={'tip': 'Average Tip ($)', 'day': 'Day of the Week'},
    template='plotly_white'
)
st.plotly_chart(fig2)  # Display the chart in Streamlit

# --- Task 3: Scatter Plot ---
st.subheader("Task 3: Scatter Plot - Tip by Total Bill by Gender")
# Scatter Plot: Tip by Total Bill by Gender
graph = px.scatter(tips, x="total_bill", y="tip", color="sex",
                   title='Tip by Total Bill by Gender',
                   labels={'total_bill': 'Total Bill ($)', 'tip': 'Tip ($)', 'sex': 'Gender'},
                   template='plotly_white')
st.plotly_chart(graph)  # Display the scatter plot in Streamlit

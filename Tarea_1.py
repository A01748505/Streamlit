import streamlit as st
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Multi-Page Dashboard", layout="wide")

page = st.sidebar.selectbox("Select an option", ["Overview", "First Chart", "Second Chart", "About"])

st.title(f"Welcome to the {page} page!")

titanic = sns.load_dataset("titanic")

if page == "Overview":
    st.write("### Overview")
    st.write("Basic Information about the dataser")
    st.write("#### Dataset Head")
    st.dataframe(titanic.head())
    st.write("#### Basic Statistics")
    st.write(titanic.describe())

    fig = px.histogram(titanic, x="age", title="Age Distribution of Titanic Passengers")
    st.plotly_chart(fig, use_container_width=True)

elif page == "First Chart":
    st.write("### First Chart")
    st.write("Analysis based on Passenger Class and Survival.")

    fig = px.box(titanic, x="pclass", y="age", color="survived", 
                 title="Passenger Age Distribution by Class and Survival Status",
                 labels={"pclass": "Passenger Class", "age": "Age", "survived": "Survived"})
    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.scatter(titanic, x="age", y="fare", color="survived", 
                      title="Fare vs. Age Colored by Survival",
                      labels={"age": "Age", "fare": "Fare", "survived": "Survived"})
    st.plotly_chart(fig2, use_container_width=True)

elif page == "Second Chart":
    st.write("### Second Chart")
    st.write("Analysis based on Sex and Embarked locations.")

    fig = px.bar(titanic, x="sex", color="embarked", barmode="group",
                 title="Passenger Count by Gender and Embarked Location",
                 labels={"sex": "Gender", "embarked": "Embarked"})
    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.pie(titanic, names="survived", title="Survival Rate on the Titanic")
    st.plotly_chart(fig2, use_container_width=True)
elif page == "About":
    st.write("### About")
    st.write("#### Cumulative Density Function of Titanic Fares")
    df = sns.load_dataset('titanic')
    df = df.dropna(subset=['fare'])
    fare_data = df['fare']
    fare_sorted = np.sort(fare_data)
    cdf_values = np.arange(1, len(fare_sorted) + 1) / len(fare_sorted)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(fare_sorted, cdf_values, marker='.', linestyle='none', color='red')
    ax.set_xlabel('Fare')
    ax.set_ylabel('Cumulative Probability')
    ax.set_title('Cumulative Density Function of Titanic Fares')
    st.pyplot(fig)
    
    fig2, ax = plt.subplots(figsize=(10, 6))
    sns.kdeplot(df['fare'], bw_adjust=0.5, fill=True, color='blue', ax=ax)
    ax.set_xlabel('Fare')
    ax.set_ylabel('Density')
    ax.set_title('Probability Density Function of Titanic Fares')
    st.pyplot(fig2)
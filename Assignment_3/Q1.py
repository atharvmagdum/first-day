import streamlit as st
import pandas as pd
import pandasql as ps
st.title("CSV Reader")

file = st.file_uploader("Upload the File :",type=["csv"])
df = []
if file:
    df = pd.read_csv(file)
    st.dataframe(df)
    query =  st.text_input("Enter the SQL Query :")

    if query:
        st.write("Query Result :")
        result = ps.sqldf(query, {"data": df})
        print("\nQuery Result:")
        st.dataframe(result)

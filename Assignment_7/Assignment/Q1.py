from langchain.chat_models import init_chat_model
import os
import pandas as pd
import streamlit as st
import pandasql as ps
from dotenv import load_dotenv
load_dotenv()

st.title("CSV Explorer")

llm = init_chat_model(
    model = "llama-3.3-70b-versatile",
    model_provider = "openai",
    base_url = "https://api.groq.com/openai/v1",
    api_key = os.getenv("GROQ_API_KEY")
)
conversation = [
    {"role": "system", "content": "You are SQLite expert developer with 10 years of experience."}
]

csv_file = st.file_uploader("Upload a CSV file: ",type=["csv"])
df = []
if csv_file:
    df = pd.read_csv(csv_file)
    st.write("CSV Table :")
    st.dataframe(df)
    st.write("CSV schema: ")
    st.write(df.dtypes)
    
    user_input = st.text_input("Ask anything about this CSV? ")
    # if user_input == "exit":
    #     break
    if user_input:
        llm_input = f"""
            Table Name: data
            Table Schema: {df.dtypes}
            Question: {user_input}
            Instruction:
                Write a SQL query for the above question. 
                Generate SQL query only in plain text format and nothing else.
                If you cannot generate the query, then output 'Error'.
        """
        result = llm.invoke(llm_input)
        st.write("Query :")
        st.write(result.content)
        query = result.content

        query_result = ps.sqldf(query,{"data":df})
        st.write("Query Result :")
        st.write(query_result)


        llm_input_2 = f"""
            Question: {result.content}
            Instruction:
                Write the simple explanation for the above SQL Query. 
                Apply the SQl Query on the uploaded csv file and give the results.
                Give the explaination in 5 lines.
        """
        result_2 = llm.invoke(llm_input_2)
        st.write("Explaination of Result :")
        st.write(result_2.content)

        



# if file:
#     df = pd.read_csv(file)
#     st.dataframe(df)
#     query =  st.text_input("Enter the SQL Query :")

#     if query:
#         st.write("Query Result :")
#         result = ps.sqldf(query, {"data": df})
#         print("\nQuery Result:")
#         st.dataframe(result)

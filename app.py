import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Database connection details
DATABASE_URL = "postgresql://postgres:postgres123@milestone2-healthcare.cz24smgc4gdj.us-east-2.rds.amazonaws.com:5432/milestone2-healthcare"

engine = create_engine(DATABASE_URL)
def fetch_data(query):
    return pd.read_sql(query, engine)

st.title("Healthcare Database Dashboard")
table_name = st.selectbox(
    "Select a Table", 
    ["admission", "admissions", "billing", "doctors", "hospitals", "medical_records", "patients"]
)

# Custom querying
query = f"SELECT * FROM public.{table_name};"
if st.button("Fetch Data"):
    try:
        data = fetch_data(query)
        st.write(f"Showing data from table: {table_name}")
        st.dataframe(data)
    except Exception as e:
        st.error(f"Error fetching data: {e}")
st.subheader("Custom SQL Query Executor")
user_query = st.text_area("Enter your SQL query below")
if st.button("Execute Query"):
    if user_query:
        try:
            user_data = fetch_data(user_query)
            st.write("Query Result:")
            st.dataframe(user_data)
        except Exception as e:
            st.error(f"Error executing query: {e}")
    else:
        st.warning("Please enter a SQL query before running.")

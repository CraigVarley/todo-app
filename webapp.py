import streamlit as st
import functions

todos = functions.get_todos()

st. title("Todo App")
st.write("Add below, select to remove.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add todo:")


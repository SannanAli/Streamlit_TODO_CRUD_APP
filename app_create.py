import streamlit as st
from db_ftnx import add_task

def run_create():
    st.subheader('CREATE YOUR TASK')

    col1,col2 = st.columns(2)

    with col1:

        task = st.text_area('Name and Details of your task',height=130,)
    
    with col2:

        task_status = st.selectbox("Task Status",['Todo','Currently Working','Completed'])

        task_due_data = st.date_input('Due Date')

    
    
    if st.button('ADD YOUR TASK!'):

        add_task(task,task_status,task_due_data)

        st.success('You have added "{}" as "{}" '.format(task,task_status))

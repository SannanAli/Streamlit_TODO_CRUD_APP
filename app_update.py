import streamlit as st
import pandas as pd
from db_ftnx import (view_data,view_unique_task,get_complete_task,add_task,update_task_data)

def run_update():
    st.subheader('Edit Or Update Your Tasks')
    created_tasks = view_data()
    #st.write(created_tasks)

    df_created_tasks = pd.DataFrame(created_tasks,columns=['Task Name','Status','Date'])

    with st.expander('Current Data'):
        st.table(df_created_tasks)

        #st.write(view_unique_task())
        list_of_tasks = [i[0] for i in view_unique_task()]
        #st.write(list_of_tasks)

        selected_task = st.selectbox('List of Tasks',list_of_tasks)

        selected_result = get_complete_task(selected_task)
        #st.write(selected_result)

        if selected_result:
            task = selected_result[0][0]
            task_status = selected_result[0][1]
            task_due_date = selected_result[0][2]
            col1,col2 = st.columns(2)

            with col1:

                new_task = st.text_area('Name and Details of your task',task,height=130)
            
            with col2:

                new_task_status = st.selectbox(task_status,['Todo','Currently Working','Completed'])

                new_task_due_data = st.date_input(task_due_date)

            
            
            if st.button('Update YOUR TASK!'):

                update_task_data(new_task,new_task_status,new_task_due_data,task,task_status,task_due_date)

                st.success('You have Successfully Updated Your Task TO "{}" FROM "{}" '.format(new_task,task))

        Updated_tasks = view_data()
        #st.write(created_tasks)

        df_updated_tasks = pd.DataFrame(Updated_tasks,columns=['Task Name','Status','Date'])

    with st.expander('Updated Data'):
            st.table(df_updated_tasks)
import streamlit  as st
from db_ftnx import view_data 
import pandas as pd
import plotly.express as px
def run_read():
    st.subheader("YOUR TASKS")

    created_tasks = view_data()
    #st.write(created_tasks)

    df_created_tasks = pd.DataFrame(created_tasks,columns=['Task Name','Status','Date'])

    with st.expander('View Your Tasks'):
        st.table(df_created_tasks)

    with st.expander('Task Status'):
        df_task = df_created_tasks['Status'].value_counts().to_frame()
        df_task_with_reset_indexes = df_task.reset_index()
        st.table(df_task_with_reset_indexes)

        pi_plot = px.pie(df_task_with_reset_indexes,names='index',values='Status')
        st.plotly_chart(pi_plot,use_container_width=True)



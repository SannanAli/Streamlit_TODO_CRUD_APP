import streamlit as st
import pandas as pd
from db_ftnx import *


def run_delete():
    st.subheader("Delete Your Task")

    result = view_data()
    df = pd.DataFrame(result,columns=['Task Name','Status','Date'])

    with st.expander('Your Current Tasks'):
        st.table(df)

        list_of_tasks = [i[0] for i in view_unique_task()]
        #st.write(list_of_tasks)

        selected_task = st.selectbox('Select Task To Delete',list_of_tasks)
        st.warning('Do You Want To Delete "{}"'.format(selected_task))
        if st.button('Delete'):

            delete_task(selected_task)
            st.success('Task Deleted Successfully')

        result_after_deleting = view_data()
        df = pd.DataFrame(result_after_deleting,columns=['Task Name','Status','Date'])

        st.table(df)

        

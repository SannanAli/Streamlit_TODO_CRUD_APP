import streamlit as st
from app_create import run_create
from db_ftnx import create_table
from app_read import run_read
from app_update import run_update
from app_delete import run_delete

def main():

    create_table()

    menu = ['Create','Read','Update','Delete','About']

    choice = st.sidebar.selectbox("Options",menu)

    if choice == 'Create':
        run_create()
    elif choice == 'Read':
        run_read()
    elif choice == 'Update':
        run_update()
    elif choice == 'Delete':
        run_delete()
    else:
        pass


if __name__ == '__main__':
    main()
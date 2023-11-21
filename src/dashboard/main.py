import streamlit as st
from initial_page import initial_page
from graphics_page import graphics_page

def main():
    # Set Wide Mode as Default
    st.set_page_config(layout="wide")

    # List of pages
    pages = {
        "Table": initial_page,
        "Graphics": graphics_page
    }

    # Select page and call
    selected_page = st.sidebar.radio("Select a page:", list(pages.keys()))
    pages[selected_page]()

if __name__ == "__main__":
    main()

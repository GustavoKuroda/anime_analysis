import streamlit as st
from animes import animes
from graphics import graphics
from home import home

def main():
    # Set Wide Mode as Default
    st.set_page_config(layout="wide")

    # List of pages
    pages = {
        "Home": home,
        "Animes": animes,
        "Graphics": graphics
    }

    # Select page and call
    selected_page = st.sidebar.radio("Select a page:", list(pages.keys()))
    pages[selected_page]()

if __name__ == "__main__":
    main()

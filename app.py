from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="우리집 플래너",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding-top: 0.7rem; padding-bottom: 0.5rem; max-width: 100%;}
    iframe {border: 0;}
</style>
""", unsafe_allow_html=True)

html_path = Path(__file__).parent / "app_ui.html"
html = html_path.read_text(encoding="utf-8")

components.html(
    html,
    height=1050,
    scrolling=True,
)

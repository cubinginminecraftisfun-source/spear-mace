import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Minecraft Attribute Practice",
    page_icon="🧱",
    layout="wide",
    initial_sidebar_state="collapsed",
)

GAME_FILE = Path(__file__).parent / "game" / "index.html"

st.markdown("""
<style>
    .block-container {padding-top: 1rem; padding-bottom: 0.5rem; max-width: 1500px;}
    header, footer {visibility: hidden;}
    [data-testid="stToolbar"] {display: none;}
</style>
""", unsafe_allow_html=True)

st.title("🧱 Minecraft Attribute Practice")
st.caption("A Minecraft-inspired, browser-based movement and hotbar practice arena.")

with st.sidebar:
    st.subheader("Practice controls")
    st.markdown("""
    - **W A S D** — move
    - **Space** — jump
    - **Shift** — sprint
    - **Mouse** — look around
    - **1–9 / scroll** — select hotbar slot
    - **Left click** — use selected item
    - **Esc** — release mouse
    - **R** — respawn
    """)
    st.divider()
    st.caption("The arena runs in your browser. Your keybind changes are stored locally in that browser.")

if not GAME_FILE.exists():
    st.error("Could not find game/index.html. Make sure you uploaded the complete project structure.")
else:
    html = GAME_FILE.read_text(encoding="utf-8")
    components.html(html, height=850, scrolling=False)

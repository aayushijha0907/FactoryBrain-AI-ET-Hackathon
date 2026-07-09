import streamlit as st
from dotenv import load_dotenv
import os

# Import frontend modules
from frontend.home import show_home
from frontend.upload import show_upload
from frontend.chat import show_chat
from frontend.dashboard import show_dashboard
from frontend.graph import show_graph

# Load environment variables
load_dotenv()

# ====================== CONFIG ======================
st.set_page_config(
    page_title="FactoryBrain AI",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/aayushijha0907/factorybrain-ai',
        'Report a bug': 'https://github.com/aayushijha0907/factorybrain-ai/issues',
    }
)

# ====================== CUSTOM STYLING ======================
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sidebar .sidebar-content {
        background-color: #f8fafc;
    }
    </style>
""", unsafe_allow_html=True)

# ====================== SIDEBAR ======================
with st.sidebar:
    st.title("🏭 FactoryBrain AI")
    st.markdown("**Industrial AI Assistant**")
    
    st.divider()
    
    page = st.radio(
        "Navigation",
        options=[
            "🏠 Home",
            "📤 Upload Documents",
            "💬 AI Chat",
            "📊 Dashboard",
            "🕸️ Knowledge Graph"
        ],
        label_visibility="collapsed"
    )
    
    st.divider()
    
    # Optional: User info / status
    st.caption("FactoryBrain AI v1.0")
    if st.button(" Refresh Data", use_container_width=True):
        st.rerun()

# ====================== MAIN CONTENT ======================
def main():
    # Page title mapping
    page_title_map = {
        "🏠 Home": "Welcome to FactoryBrain AI",
        "📤 Upload Documents": "Document Upload & Processing",
        "💬 AI Chat": "AI Assistant Chat",
        "📊 Dashboard": "Factory Intelligence Dashboard",
        "🕸️ Knowledge Graph": "Knowledge Graph Explorer"
    }
    
    st.markdown(f"<h1 class='main-header'>{page_title_map.get(page, 'FactoryBrain AI')}</h1>", 
                unsafe_allow_html=True)
    
    # Route to the appropriate page
    if page == "🏠 Home":
        show_home()
    elif page == "📤 Upload Documents":
        show_upload()
    elif page == "💬 AI Chat":
        show_chat()
    elif page == "📊 Dashboard":
        show_dashboard()
    elif page == "🕸️ Knowledge Graph":
        show_graph()

if __name__ == "__main__":
    main()

# ====================== FOOTER ======================
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #64748b; font-size: 0.8rem;'>
        FactoryBrain AI © 2026 | Built with ❤️ for Smart Manufacturing
    </div>
    """, 
    unsafe_allow_html=True
)

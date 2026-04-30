import streamlit as st
from sktime_agent.core import generate_response

st.set_page_config(
    page_title="Agentic sktime Assistant",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS for premium feel
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stTextInput > div > div > input {
        background-color: #262730;
        color: white;
        border-radius: 10px;
    }
    .stButton > button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        width: 100%;
    }
    .code-box {
        background-color: #1e1e1e;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #333;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 Agentic sktime Assistant")
st.subheader("LLM-driven Time Series Workflow Generator")

query = st.text_input("Enter your time series task (e.g., 'forecast sales for 12 months')", 
                     placeholder="How can I help you with sktime today?")

use_agent = st.checkbox("Use real LLM agent (requires API keys)", value=False)

if st.button("Generate Workflow"):
    if query:
        with st.spinner("Analyzing intent and generating sktime pipeline..."):
            try:
                response = generate_response(query, use_agent=use_agent)
                
                col1, col2 = st.columns([1, 1])
                
                with col1:
                    st.info(f"**Task Type:** {response.task_type.capitalize()}")
                    st.markdown(f"### Explanation\n{response.explanation}")
                
                with col2:
                    st.markdown("### Generated sktime Code")
                    st.code(response.code, language="python")
                    
                    if response.evaluation:
                        st.markdown("### Evaluation Snippet")
                        st.code(response.evaluation, language="python")
            except Exception as e:
                st.error(f"Error generating response: {str(e)}")
    else:
        st.warning("Please enter a query first.")

st.markdown("---")
st.markdown("Built for the **Enabling sktime Ecosystem (ESoC)** initiative.")

import streamlit as st
import requests

# 1. Page Configuration (Sets the browser tab title and icon)
st.set_page_config(page_title="L&D Knowledge Portal", page_icon="🎓")

# --- Custom Styling for L&D Look ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar for Learning Resources
with st.sidebar:
    st.header("📚 Learning Center")
    st.info("Ask our AI Mentor about your current curriculum or professional development goals.")
    st.divider()
    st.subheader("Quick Links")
    st.caption("- Company Handbook")
    st.caption("- Q3 Training Calendar")

# 3. Main UI Header
st.title("🎓 L&D AI Mentor")
st.subheader("Personalized Upskilling Assistant")
st.write("Enter your learning query or topic below to receive guided insights from our knowledge base.")

# 4. User Input Area
user_input = st.text_area("What would you like to learn about today?", placeholder="e.g., How do I improve my project management skills?")

# 5. Submit Action
if st.button("Consult AI Mentor"):
    if user_input:
        # Using a status spinner for a professional feel
        with st.status("Searching knowledge base...", expanded=True) as status:
            API_URL = "http://127.0.0.1:5000/ask"
            payload = {"question": user_input}
            
            try:
                response = requests.post(API_URL, json=payload)
                result = response.json()
                
                status.update(label="Insight Generated!", state="complete", expanded=False)
                
                # Display results in a clean container
                st.markdown("### 💡 Guidance")
                st.info(result["answer"])
                
                # Professional L&D touch: Feedback loop
                st.divider()
                st.caption("Was this helpful for your learning path?")
                col1, col2 = st.columns([1, 10])
                col1.button("👍")
                col2.button("👎")

            except Exception as e:
                status.update(label="Connection Error", state="error")
                st.error("The L&D server is currently offline. Please contact IT.")
    else:
        st.warning("Please enter a question to start your learning session.")
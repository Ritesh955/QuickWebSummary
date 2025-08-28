import streamlit as st
from utils import display_summary  # Make sure your `summarize` function is correctly imported

st.set_page_config(page_title="SummaryAI", layout="centered")
st.title("🔍 WebSummaryAI")
st.subheader("Know website summary. Instantly!")

# Input for URL
url = st.text_input("Enter a website URL:")

# Button to trigger summarization
if st.button("Summarize") and url:
    with st.spinner("Analyzing the site..."):
        try:
            summary = display_summary(url)
            st.markdown("### Summary")
            st.write(summary)

            # Download button for the summary
            st.download_button("📄 Export Summary", summary, file_name="summary.md")
        except Exception as e:
            st.error(f"An error occurred: {e}")
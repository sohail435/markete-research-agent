import streamlit as st
from scraper import fetch_market_data
from agent import analyze_competitor_data

# Set up the webpage title and icon
st.set_page_config(page_title="AI Market Research Agent", page_icon="🧠")

st.title("🚀 Automated Market Research Agent")
st.markdown("""
This intelligent agent scrapes a competitor's website text and uses **Gemini 2.5 Flash** to extract deep market insights like brand positioning, features, pricing, and target audience.
""")

st.write("---")

# User Input: URL text box
target_url = st.text_input("Enter Competitor Website URL:", placeholder="https://example.com")

# Action Button
# Action Button
if st.button("Run Market Intelligence Analysis"):
    # Clean up any accidental leading/trailing spaces
    cleaned_url = target_url.strip()
    
    if not cleaned_url:
        st.warning("⚠️ Please enter a competitor URL first!")
    elif "\\" in cleaned_url:
        st.error("❌ Invalid URL format. Please use forward slashes (//) instead of backslashes (\\).")
    elif not cleaned_url.startswith(("http://", "https://")):
        st.error("❌ Invalid URL. Please make sure it starts with http:// or https://")
    else:
        with st.spinner("🕵️‍♂️ Agent is fetching data and analyzing... Please wait..."):
            try:
                # 1. Perception Phase using the cleaned URL
                raw_data = fetch_market_data(cleaned_url)
                
                # 2. Reasoning Phase
                analysis_result = analyze_competitor_data(raw_data)
                
                # 3. Output Phase
                st.success("Analysis Complete!")
                st.subheader("📊 Market Intelligence Report")
                st.markdown(analysis_result)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
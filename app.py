import streamlit as st
from scraper import fetch_market_data
from agent import analyze_market_data, chat_with_report

st.title("🚀 Automated Market Research Agent")
st.write("This intelligent agent scrapes a competitor's website text and uses Gemini 2.5 Flash to generate deep marketing insights.")

# User Input
competitor_url = st.text_input("Enter Competitor Website URL:", placeholder="https://example.com")

# 🧠 STEP 1: Initialize all session state trackers
if "market_report" not in st.session_state:
    st.session_state.market_report = None
if "current_url" not in st.session_state:
    st.session_state.current_url = ""
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Trigger analysis only if the button is clicked
if st.button("Generate Market Insights"):
    if not competitor_url.strip():
        st.warning("Please enter a valid website URL first.")
    else:
        with st.spinner("Scraping website and generating deep insights with Gemini..."):
            try:
                # STEP 2: Clear old data if the user changes the URL target
                if st.session_state.current_url != competitor_url:
                    st.session_state.market_report = None
                    st.session_state.current_url = competitor_url
                    st.session_state.chat_history = []  # Reset timeline for fresh site

                # Fetch raw content and run your core analyzer
                raw_text = fetch_market_data(competitor_url)
                report = analyze_market_data(raw_text)

                # Save report results into session state memory
                st.session_state.market_report = report

            except Exception as e:
                st.error(f"An error occurred: {e}")

# STEP 3: Display the saved report if it exists in memory
if st.session_state.market_report:
    st.success("Analysis Complete!")
    st.markdown("---")
    st.markdown(st.session_state.market_report)
    st.markdown("---")

    # 💬 STEP 4: Build out the Conversational Memory Stream UI
    st.subheader("💬 Ask Follow-up Questions About This Report")

    # Loop through historical log and draw previous chat messages
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept new conversational input from user
    if user_question := st.chat_input("Ask something about the competitor insights..."):
        # Display typed message live in UI
        with st.chat_message("user"):
            st.markdown(user_question)
        
        # Log message into history array cache
        st.session_state.chat_history.append({"role": "user", "content": user_question})

        # Request reply from agent using report context
        with st.spinner("Thinking..."):
            try:
                ai_response = chat_with_report(st.session_state.market_report, user_question)
            except Exception as e:
                ai_response = f"Could not fetch answer: {e}"
            
        # Display assistant reply live in UI
        with st.chat_message("assistant"):
            st.markdown(ai_response)
        
        # Log assistant reply into history array cache
        st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
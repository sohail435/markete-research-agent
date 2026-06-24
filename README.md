# 🚀 Automated Market Research Agent

![Market Research Agent Banner](banner.png)

An intelligent web scraping and AI analytics agent that extracts competitor website data and leverages Gemini 2.5 Flash to generate deep market research insights. Built entirely in Python and deployed as a live interactive web application.

---

## 🔗 Project Links
* **Live Web Application:** [Streamlit Cloud App](https://share.streamlit.io/sohail435/markete-research-agent/main/app.py)
* **Source Repository:** [GitHub Page](https://github.com/sohail435/markete-research-agent)

## 📌 Current Version: v1.1.0 (Robust Scraping Layer)
The application has moved past its initial MVP stage to include production-grade security and client emulation:
* **Dynamic Header Spoofing:** Integrated `fake-useragent` to inject randomized, authentic desktop browser fingerprints (Chrome, Firefox, Edge) to safely bypass basic bot-detection firewalls.
* **Semantic Versioning:** Fully structured repository history using Git tags (`v1.0.0` for original unmasked MVP, `v1.1.0` for robust scraper).

## 🛠️ Tech Stack & Utilities
* **Frontend UI:** Streamlit
* **AI Engine:** Google Gemini 2.5 Flash API (`google-genai`)
* **Scraping Engine:** Requests + BeautifulSoup4
* **Security Layer:** Fake-UserAgent (Dynamic Browser Profiling)

## 📦 Installation & Local Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/sohail435/markete-research-agent.git](https://github.com/sohail435/markete-research-agent.git)
   cd markete-research-agent
import os
from dotenv import load_dotenv
from google import genai
from scraper import fetch_market_data

# Load the token from the .env file
load_dotenv()

# Fetch the specific key
api_key = os.environ.get("GEMINI_API_KEY")

# Initialize the client with our secure API key
client = genai.Client(api_key=api_key)

# 🌟 PRESERVED BRAND NAME FUNCTION
def analyze_market_data(raw_html_text):
    # 1. Define our targeted instructions
    analysis_prompt = f"""
    You are an expert market research assistant. 
    Analyze the following raw competitor text and extract these details:
    1. Brand Name: Identify the company or product name.
    2. Features: List the key features or capabilities offered.
    3. Pricing: Extract any pricing tiers, subscription costs, or free trial info.
    4. Target Market: Identify who this product is built for.

    Raw Text:
    {raw_html_text}
    """
    
    # 2. Send the combined prompt to the model
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=analysis_prompt
    )
    
    # 3. Return the AI's analysis
    return response.text

# 💬 NEW FOR V1.2.0: Follow-up Chat Function using your existing client
def chat_with_report(report_context, user_question):
    """
    Sends the user's follow-up question to Gemini along with the 
    previously generated market report to serve as context.
    """
    prompt = f"""
    You are an expert market research assistant. You previously generated the following market report:
    
    ---
    {report_context}
    ---
    
    Based strictly on the report context provided above, please answer the following follow-up user question. 
    If the answer cannot be inferred from the report, state that you don't have that specific data but provide a helpful, relevant marketing perspective.
    
    User Question: {user_question}
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )
    return response.text

if __name__ == "__main__":
    target_url = "https://example.com" 
    
    print("Fetching data...")
    raw_data = fetch_market_data(target_url)
    
    print("Analyzing data with Gemini...")
    analysis_result = analyze_market_data(raw_data)
    
    print("\n--- Market Intelligence Report ---")
    print(analysis_result)
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
def analyze_competitor_data(raw_html_text):
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
if __name__ == "__main__":
    # A test URL (you can replace this with a real competitor site later)
    target_url = "https://example.com" 
    
    print("Fetching data...")
    raw_data = fetch_market_data(target_url)
    
    print("Analyzing data with Gemini...")
    analysis_result = analyze_competitor_data(raw_data)
    
    print("\n--- Market Intelligence Report ---")
    print(analysis_result)
import requests
from bs4 import BeautifulSoup

def fetch_market_data(url: str) -> str:
    """
    Fetches raw text content from a target URL using a standard HTTP request.
    (Basic v1.0.0 MVP Version)
    """
    try:
        # Standard unmasked HTTP request
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse text content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove invisible script and style elements
        for script in soup(["script", "style"]):
            script.extract()
            
        return soup.get_text(separator=" ", strip=True)
        
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch website data: {e}")
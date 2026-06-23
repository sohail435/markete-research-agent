import requests

def fetch_market_data(url):
    #We will use requests to get the web page data here
    respose = requests.get(url)
    #This returns the raw HTML text so our agent can read it
    return respose.text

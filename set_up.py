#Import Packages
import requests

#API Calls

# Create API call function
def fetch_data_from_api(api_endpoint, params):
    try:
        response = requests.get(api_endpoint, params=params)
    
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"API request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"An error occurred: {e}")
    
#Call National Weather Service API - "https://api.weather.gov/"

api_endpoint = "https://api.weather.gov/"
params = {}
data = fetch_data_from_api(api_endpoint, params)
print(data)

# Call Real Estate API - 
# Here is a link with a list to choose from: https://gist.github.com/patpohler/36c731113fd113418c0806f62cbb9e30



    
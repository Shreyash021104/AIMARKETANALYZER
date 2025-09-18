api_key="pAGGRPUvPWs8bCS4miZzrLdZ"
import requests

url = "https://www.searchapi.io/api/v1/search"
params = {
  "engine": "meta_ad_library_page_search",
  "q": "tesl",
  "api_key": "pAGGRPUvPWs8bCS4miZzrLdZ"
}

response = requests.get(url, params=params)
print(response.text)
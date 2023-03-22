import requests 
url = "https://json.org/example.html"

response = requests.get(url)
print(response.text)
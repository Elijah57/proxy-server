import requests

# Set up proxy settings
proxies = {
    'http': 'http://127.0.0.1:8080',
}

# Make a request through the proxy
response = requests.get('http://google.com', proxies=proxies)

print(response.text)

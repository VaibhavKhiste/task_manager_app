import requests

def fetch_external_todos():
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()[:10]  # limit to 10 items

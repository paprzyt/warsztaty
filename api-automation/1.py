import requests

url = "https://jsonplaceholder.typicode.com/posts"

resp = requests.get(url + "/1")
data = {"userID": 99, "id": 1, "title": "Test", "body": "Very long test"}
requests.put(url + "/1", json=data)

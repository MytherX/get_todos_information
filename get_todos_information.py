import requests

url = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(url)
todos = response.json()

# Išvedame pirmųjų 10 užduočių pavadinimus su numeracija
for index, todo in enumerate(todos[:10], start=1):
    print(f"{index}. {todo['title']}")

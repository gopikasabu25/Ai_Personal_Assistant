import requests

url = "http://127.0.0.1:5000/chat"

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    payload = {
        "user_id": "user1",
        "message": user_input
    }

    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        print("Agent:", response.json()["response"])
    else:
        print("Something went wrong:", response.status_code)

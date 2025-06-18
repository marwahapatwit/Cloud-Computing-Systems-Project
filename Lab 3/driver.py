import requests

base = "http://127.0.0.1:8000"

# Test GET routes
print("GET /:", requests.get(f"{base}/").json())
print("GET /greet:", requests.get(f"{base}/greet", params={"name": "Pranav"}).json())
print("GET /square:", requests.get(f"{base}/square", params={"num": 8}).json())
print("GET /event/PopUp:", requests.get(f"{base}/event/PopUp").json())
print("GET /item/studios/5:", requests.get(f"{base}/item/studios/5").json())

# Test PUT routes
print("PUT /submit-feedback:", requests.put(f"{base}/submit-feedback", json={"rating": 5, "comment": "Amazing!"}).json())
print("PUT /rsvp:", requests.put(f"{base}/rsvp", json={"name": "Pranav", "event": "Run Club"}).json())

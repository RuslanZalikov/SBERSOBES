import requests

resp = requests.get("http://0.0.0.0:9091/models")
# resp = requests.post("http://localhost:8080/predictions/TEST1", json={"data": "Hello love"})
print(resp.text)
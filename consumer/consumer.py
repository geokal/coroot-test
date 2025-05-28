import requests

def consume():
    with requests.get("http://producer:9005/stream", stream=True) as resp:
        for line in resp.iter_lines():
            if line:
                print(f"Consumer received: {line.decode()}")

if __name__ == "__main__":
    consume()

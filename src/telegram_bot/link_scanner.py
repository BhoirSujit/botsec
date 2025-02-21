import requests
from config import SERVER_HOST, SERVER_PORT

# Check if the link is malicious or not
def check_link(link):

    server_address = f"http://{SERVER_HOST}:{SERVER_PORT}/verifylink"
    print(f"🔍 Checking link: {link} at {server_address}")

    payload = {"link": link} 

    try:
        response = requests.post(server_address, json=payload) 
        response.raise_for_status() 
        data = response.json()
        print("✅ Response:", data)

        #determine if link is malicious or safe
        if data.get("is_malicious"):
            return f"⚠️ Malicious link detected: {link}"
        else:
            return f"✅ Safe link: {link}"
        
    except requests.HTTPError as err:
        print(f"❌ HTTP Error: {err}")
    except requests.RequestException as err:
        print(f"❌ Request Failed: {err}")

    return "❌ Unable to check link due to an error."

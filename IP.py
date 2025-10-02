import requests

def get_public_ip():
    """Fetch your public IP using a free API."""
    try:
        response = requests.get("https://api.ipify.org", timeout=5)
        return response.text
    except Exception:
        return "Unable to fetch IP"

# Example
print("Your public IP:", get_public_ip())
# Output: Your public IP: 203.0.113.45

# utils/api_utils.py
import requests

def realizar_llamada_api(url, headers=None, payload=None, method="GET"):
    try:
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, json=payload, headers=headers)
        
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error en la llamada API: {e}")
        return None

import requests
import os
from langchain.tools import Tool
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

SHOPIFY_API_KEY = os.getenv("SHOPIFY_API_KEY")
SHOPIFY_PASSWORD = os.getenv("SHOPIFY_PASSWORD")
SHOPIFY_STORE_URL = os.getenv("SHOPIFY_STORE_URL")

def consultar_inventario_shopify(product_id):
     print(f"Checking inventory for product: {product_id}")
    url = f"{SHOPIFY_STORE_URL}/admin/api/2023-01/products/{product_id}.json"
    response = requests.get(url, auth=(SHOPIFY_API_KEY, SHOPIFY_PASSWORD))
    
    # Imprimir la respuesta de la API para depuración
     print(f"Inventory Response Status Code: {response.status_code}")
    print(f"Inventory Response Content: {response.text}")
    
    return response.json()

def actualizar_inventario_shopify(product_id, cantidad):
    url = f"{SHOPIFY_STORE_URL}/admin/api/2023-01/inventory_levels/set.json"
    payload = {"location_id": "tu_location_id", "inventory_item_id": product_id, "available": cantidad}
    response = requests.post(url, json=payload, auth=(SHOPIFY_API_KEY, SHOPIFY_PASSWORD))
    
    # Imprimir la respuesta de la API para depuración
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")
    
    return response.json()

# Definir las herramientas para LangChain
inventory_tool = Tool(
    name="ConsultarInventario",
    func=consultar_inventario_shopify,
    description="Consulta el inventario de un producto en Shopify, regresa un numero"
)

update_inventory_tool = Tool(
    name="ActualizarInventario",
    func=actualizar_inventario_shopify,
    description="Actualiza el inventario de un producto en Shopify"
)

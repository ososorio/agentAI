from fastapi import FastAPI
from agents.shopify_agent import create_shopify_agent

app = FastAPI()

# Crear el agente de Shopify
shopify_agent = create_shopify_agent()

@app.get("/inventory")
async def get_inventory(product_id: str):
    """
    Llama al agente de Shopify para obtener el inventario de un producto usando su ID.
    """
    try:
        # Asegúrate de usar 'input' como clave en el diccionario
        result = shopify_agent.run({"input": product_id})
        return {"inventory": result}
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
async def root():
    return {"message": "API de Shopify con LangChain"}

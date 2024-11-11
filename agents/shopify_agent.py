from langchain.agents import Tool, AgentExecutor, AgentType, initialize_agent
from langchain_openai import ChatOpenAI
import openai
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Función para verificar inventario en Shopify
def check_inventory(query: str) -> str:
    # Implementar la lógica de interacción con Shopify aquí
    return f"Checking inventory for: {query}"

# Definir la clase de herramienta para Shopify
class ShopifyInventoryTool(Tool):
    def __init__(self):
        super().__init__(
            name="Shopify Inventory Tool",
            func=check_inventory,
            description="Tool to interact with Shopify API to check inventory levels"
        )

# Crear el agente de Shopify
def create_shopify_agent():

    # Crear el cliente LLM (ChatOpenAI)
    try:
        print("Creando LLM...")
        llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY)  # Crear el modelo LLM
        print("LLM creado correctamente.")
    except Exception as e:
        print(f"Error al crear el modelo LLM: {e}")
        return None

    # Crear la herramienta de Shopify
    try:
        print("Creando herramienta de Shopify...")
        shopify_tool = ShopifyInventoryTool()
        print("Herramienta Shopify creada correctamente.")
    except Exception as e:
        print(f"Error al crear la herramienta Shopify: {e}")
        return None

    # Inicializar el agente con la herramienta y el modelo de lenguaje
    try:
        print("Creando el agente...")
        agent = initialize_agent(
            tools=[shopify_tool],  # Pasamos la herramienta aquí
            llm=llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # Tipo de agente
            verbose=True  # Activar salida detallada
        )
        print("Agente creado correctamente.")
    except Exception as e:
        print(f"Error al crear el agente: {e}")
        return None

    return agent

# Ejecutar el agente con una consulta
if __name__ == "__main__":
    agent = create_shopify_agent()

    if agent is None:
        print("El agente no se pudo crear correctamente.")
    else:
        # Realizar la consulta
        query = "product X"  # Ejemplo de producto a consultar
        try:
            response = agent.run(query)
            print(f"Respuesta del agente: {response}")
        except Exception as e:
            print(f"Error al ejecutar el agente: {e}")

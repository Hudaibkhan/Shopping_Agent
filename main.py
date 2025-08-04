from connection import config
from agents import Agent, Runner, function_tool
import requests
import asyncio

# Tool: Fetch and return combined product data from two APIs
@function_tool
def get_combined_products():
    try:
        response_1 = requests.get("https://hackathon-apis.vercel.app/api/products")
        response_2 = requests.get("https://next-ecommerce-template-4.vercel.app/api/product")
        data1 = response_1.json()
        data2 = response_2.json()

        products = []

        # Normalize data from first API
        if isinstance(data1, list):
            products.extend(data1)
        elif isinstance(data1, dict) and "products" in data1:
            products.extend(data1["products"])

        # Normalize data from second API
        if isinstance(data2, list):
            products.extend(data2)
        elif isinstance(data2, dict) and "products" in data2:
            products.extend(data2["products"])

        return {"products": products}
    
    except Exception as e:
        return {"error": str(e), "products": []}

# Create the shopping assistant agent
agent = Agent(
    name="Shopping Agent",
    instructions=(
        "You are a smart shopping assistant. Use the product data to directly recommend or list the best products under a budget. "
        "Do not ask the user any questions. Just suggest helpful options clearly, even if some details are missing."
    ),
    tools=[get_combined_products],
)

# Main runner
async def main():
    result = await Runner.run(
        agent,
        "Give some bed options",
        run_config=config
    )
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
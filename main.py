from agents import Agent , Runner , function_tool
from connection import config
from dotenv import load_dotenv
import requests
import asyncio

load_dotenv()

@function_tool
def product_details():
    api_one = requests.get("https://hackathon-apis.vercel.app/api/products")
    api_two = requests.get("https://next-ecommerce-template-4.vercel.app/api/product")
    api_one_data = api_one.json()
    api_two_data = api_two.json()
    return api_one_data , api_two_data
  
    
shopping_agent =Agent(
    name="Shopping Agent",
    instructions="You are a helpful shopping assistant that recommends products to users"
)

async def main():
    result = await Runner.run(
        shopping_agent,
        "Show me electronics under $100",
        run_config=config
    )
    print(result.final_output)
    
if __name__ == "__main__":
    asyncio.run(main())
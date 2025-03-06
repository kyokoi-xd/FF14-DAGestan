import aiohttp
import asyncio

BASE_URL = "https://universalis.app/api"
XIVAPI_URL = "https://xivapi.com"

async def get_ids_items():
    async with aiohttp.ClientSession() as session:
        url = f"{XIVAPI_URL}/Shop"
        async with session.get(url) as response:
            data = await response.json()
            return data
    
async def filter_items_for_gil():
    items = await get_ids_items()
    gil_items = [item for item in items if item.get("Cost", {}).get("Gil")]
    return gil_items

async def main():
    gil_items = await filter_items_for_gil()
    print(f"Найдено {len(gil_items)} предметов, продаваемых за гилы у NPC")
    for item in gil_items[:10]:
        print(item)

if __name__ == "__main__":
    asyncio.run(main())
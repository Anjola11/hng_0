
import httpx

CAT_FACT_URL = "https://catfact.ninja/fact"

async def fetch_cat_fact() -> str:
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(CAT_FACT_URL)
            response.raise_for_status()
            data = response.json()
            return data.get("fact", "No fact available at the moment.")
    except Exception:
        return "Could not fetch cat fact at the moment. Please try again later."

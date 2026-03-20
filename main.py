from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import httpx
import os

app = FastAPI()

# URL server chính để proxy API
MAIN_SERVER = "https://chiaki-web-get-order.onrender.com"

@app.get("/", response_class=HTMLResponse)
async def index():
    with open("static/phone.html", encoding="utf-8") as f:
        return f.read()

# Proxy /api/order-info về server chính
@app.post("/api/order-info")
async def proxy_order_info(body: dict):
    async with httpx.AsyncClient(timeout=20) as client:
        res = await client.post(
            f"{MAIN_SERVER}/api/order-info",
            json=body
        )
        return res.json()

# Proxy check-key
@app.post("/api/order-info/check-key")
async def proxy_check_key(body: dict):
    async with httpx.AsyncClient(timeout=10) as client:
        res = await client.post(
            f"{MAIN_SERVER}/api/order-info/check-key",
            json=body
        )
        return res.json()

import json
from urllib import response
from fastapi import FastAPI, Request
import requests

app = FastAPI()

@app.post("/burn_callbacks/search")
async def callbacks_search(request: Request):
    json1 = await request.json()
    response = requests.post("https://api.octusbridge.io/v1/dao/burn_callbacks/search", json=json1)
    return response.json()

@app.post("/dao/search/stakeholders")
async def stakeholders_search(request: Request):
    json1 =await request.json()
    response = requests.post("https://api.octusbridge.io/v1/dao/search/stakeholders", json=json1)
    return response.json()

@app.get("/dao/user/{user_address}")
async def read_item(user_address):
    response = requests.get("https://api.octusbridge.io/v1/dao/user/" + user_address) 
    return response.json()

@app.post("/relays_pages/relay_info")
async def relay_info(request: Request):
    json1 = await request.json()
    response = requests.post("https://api.octusbridge.io/v1/relays_pages/relay_info", json=json1)
    return response.json()

    
@app.post("/relays_pages/relay_round_info")
async def relay_round_info(request: Request):
    json1 = await request.json()
    response = requests.post("https://api.octusbridge.io/v1/relays_pages/relay_round_info", json=json1)
    return response.json()

@app.post("/relays_pages/relays_round_info")
async def relays_round_info(request: Request):
    json1 = await request.json()
    response = requests.post("https://api.octusbridge.io/v1/relays_pages/relays_round_info", json=json1)
    return response.json()

@app.post("/relays_pages/all_relay_rounds_info")
async def all_relays_round_info(request: Request):
    json1 = await request.json()
    response = requests.post("https://api.octusbridge.io/v1/relays_pages/all_relay_rounds_info", json=json1)
    return response.json()

@app.post("/relays_pages/round_info")
async def round_info(request: Request):
    json1 = await request.json()
    response = requests.post("https://api.octusbridge.io/v1/relays_pages/round_info", json=json1)
    return response.json()

@app.post("/relays_pages/search/relays")
async def search_relays(request: Request):
    json1 = await request.json()
    response = requests.post("https://api.octusbridge.io/v1/relays_pages/search/relays", json=json1)
    return response.json()

@app.post("/relays_pages/search/relays_events")
async def search_relays_events(request: Request):
    json1 = await request.json()
    response = requests.post("https://api.octusbridge.io/v1/relays_pages/search/relays_events", json=json1)
    return response.json()

@app.post("/relays_pages/search/global_relays_events")
async def search_global_relays_events(request: Request):
    json1 = await request.json()
    response = requests.post("https://api.octusbridge.io/v1/relays_pages/search/global_relays_events", json=json1)
    return response.json()

@app.post("/relays_pages/rounds_calendar")
async def rounds_calendar(request: Request):
    json1 = await request.json()
    response = requests.post("https://api.octusbridge.io/v1/relays_pages/rounds_calendar", json=json1)
    return response.json()

@app.post("/relays_pages/relay_rounds_info")
async def relay_rounds_info(request: Request):
    json1 = await request.json()
    response = requests.post("https://api.octusbridge.io/v1/relays_pages/relay_rounds_info", json=json1)
    return response.json()

@app.post("/staking/search/stakeholders")
async def staking_search_stakeholders(request: Request):
    json1 = await request.json()
    response = requests.post("https://api.octusbridge.io/v1/staking/search/stakeholders", json=json1)
    return response.json()

@app.post("/staking/search/transactions")
async def staking_search_transactions(request: Request):
    json1 = await request.json()
    response = requests.post("https://api.octusbridge.io/v1/staking/search/transactions", json=json1)
    return response.json()

@app.post("/staking/graph/tvl")
async def staking_graph_tvl(request: Request):
    json1 = await request.json()
    response = requests.post("https://api.octusbridge.io/v1/staking/graph/tvl", json=json1)
    return response.json()

@app.post("/staking/graph/apr")
async def staking_graph_apr(request: Request):
    json1 = await request.json()
    response = requests.post("https://api.octusbridge.io/v1/staking/graph/apr", json=json1)
    return response.json()

@app.get("/staking/main")
async def staking_main():
    response = requests.get("https://api.octusbridge.io/v1/staking/main") 
    return response.json()

@app.post("/staking")
async def staking_user(request: Request):
    json1 = await request.json()
    response = requests.post("https://api.octusbridge.io/v1/staking", json=json1)
    return response.json()

@app.post("/transfers/search")
async def transfers_search(request: Request):
    json1 = await request.json()
    response = requests.post("https://api.octusbridge.io/v1/transfers/search", json=json1)
    return response.json()

@app.post("/transfers/search_not_instant")
async def transfers_search_not_instant(request: Request):
    json1 = await request.json()
    response = requests.post("https://api.octusbridge.io/v1/transfers/search_not_instant", json=json1)
    return response.json()

@app.get("/transfers/main_page")
async def transfers_main():
    response = requests.get("https://api.octusbridge.io/v1/transfers/main_page") 
    return response.json()

@app.post("/transfers/graph/volume")
async def transfers_graph_volume(request: Request):
    json1 = await request.json()
    response = requests.post("https://api.octusbridge.io/v1/transfers/graph/volume", json=json1)
    return response.json()
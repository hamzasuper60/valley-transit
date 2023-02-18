from sanic import Request
from sanic.response import  HTTPResponse, json
from json import loads
from datetime import datetime

async def handler(request: Request) -> HTTPResponse:
    response = list()
    bus_stop_list = sorted(request.app.ctx.CONFIG["bus_stops"], key=lambda x: x['name'])
    for bus_stop in bus_stop_list:
        routes = []
        for times in bus_stop["times"]:
            routes.append(int(times["route"]))
        routes = list(dict.fromkeys(routes))
        routes = sorted(routes)
        response.append({
        "name": bus_stop["name"],
        "postal": bus_stop["postal"],
        "id": bus_stop["id"],
        "routes": routes
    })
    return json(response)
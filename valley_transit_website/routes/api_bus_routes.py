from sanic import Request
from sanic.response import  HTTPResponse, json
from json import loads
from datetime import datetime

async def handler(request: Request) -> HTTPResponse:
    response = list()
    bus_route_list = sorted(request.app.ctx.CONFIG["bus_routes"], key=lambda x: x['route'])
    for bus_route in bus_route_list:
        response.append(bus_route)
    return json(response)
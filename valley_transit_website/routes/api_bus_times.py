from sanic import Request
from sanic.response import  HTTPResponse, json
from json import loads
from datetime import datetime

def get_bus_route_status() -> dict:
    with open('./data/bus_route_status.json') as f:
        return loads(f.read())


def get_bus_stop_info(request: Request) -> dict:
    bus_stop_info = None
    for bus_stop in request.app.ctx.CONFIG["bus_stops"]:
        if bus_stop["id"] == request.args.get('bus_stop'):
            bus_stop_info = bus_stop
    return bus_stop_info

async def handler(request: Request) -> HTTPResponse:
    bus_stop_info = get_bus_stop_info(request)
    if bus_stop_info is None:
        return json({"error": True})
    status = get_bus_route_status()
    time = datetime.now()
    res = []
    for bus_stop_time in bus_stop_info["times"]:
        if not status[f"route_{bus_stop_time['route']}"]:
            continue
        departs_in = bus_stop_time["departure"] - time.minute
        if departs_in < 0:
            departs_in = departs_in + 60
        res.append({
                "route": bus_stop_time["route"],
                "destination": bus_stop_time["destination"],
                "departs_in": departs_in
            },)
    res = sorted(res, key=lambda x: x['departs_in'])
    return json({"info": {
        "name": bus_stop_info["name"],
        "postal": bus_stop_info["postal"]
    },
    "times": res
    })
from sanic import Request
from sanic.response import HTTPResponse, html
from json import loads, dumps


async def handler(request: Request) -> HTTPResponse:
    with open('./data/bus_route_status.json') as f:
        route_status = loads(f.read())
    key = request.args.get('key')
    route = request.args.get('route')
    if key != "REDACTED":
        return html('<script>alert("The access key provided was invalid.");</script>')
    try:
        current_status = route_status[f"route_{route}"]
    except KeyError:
        return html('<script>alert("The route provided was not found.");</script>')
    if current_status:
        return html('<script>alert("The route is already being operated.");</script>')
    route_status[f"route_{route}"] = True
    with open('./data/bus_route_status.json', 'w') as f:
        f.write(dumps(route_status))
    return html('<script>alert("The route has been activated.");</script>')
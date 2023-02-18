from json import loads

def load_sanic_config() -> dict:
    with open('./sanic.config.json', 'r') as file:
        content = file.read()
        json = loads(content)
        return json

def load_routing_config() -> dict:
    with open('./routing.config.json', 'r') as file:
        content = file.read()
        json = loads(content)
        return json

def load_custom_config() -> dict:
    with open('./data/limo_list.json', 'r') as file:
        content = file.read()
        limo_list = loads(content)
    with open('./data/bus_stops.json', 'r') as file:
        content = file.read()
        bus_stops = loads(content)
    with open('./data/bus_routes.json', 'r') as file:
        content = file.read()
        bus_routes = loads(content)
    return {
        "limo_list": limo_list,
        "bus_stops": bus_stops,
        "bus_routes": bus_routes
    }
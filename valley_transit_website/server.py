# Static Imports
from os import listdir
from os.path import isfile, join
from sanic import Sanic
from shared.config import load_sanic_config, load_routing_config, load_custom_config

# Dynamic Imports
routes = [f for f in listdir("./routes") if isfile(join("./routes", f))]
for route in routes:
    exec(
        f"from routes.{route.replace('.py', '')} import handler as route_{route.replace('.py', '')}_handler", globals())

# App Creation
sanic_config = load_sanic_config()
app = Sanic(sanic_config["name"])
app.static('/assets', './assets')
app.ctx.CONFIG = load_custom_config()

# Route Registering
routing_config = load_routing_config()
for route in routing_config:
    exec(
        f"app.add_route({route['handler']}, '{route['path']}', methods={route['methods']})")

if __name__ == "__main__":
    app.run(
        host=sanic_config["host"],
        port=sanic_config["port"],
        debug=sanic_config["debug"],
        auto_reload=sanic_config["auto_reload"],
        access_log=sanic_config["access_log"],
        fast=sanic_config["fast"]
    )
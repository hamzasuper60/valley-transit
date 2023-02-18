from sanic import Request
from sanic.response import  HTTPResponse, json

async def handler(request: Request) -> HTTPResponse:
    return json(request.app.ctx.CONFIG["limo_list"])
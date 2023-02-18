from sanic import Request
from sanic.response import  HTTPResponse, file

async def handler(request: Request) -> HTTPResponse:
    return await file('./views/base.html')
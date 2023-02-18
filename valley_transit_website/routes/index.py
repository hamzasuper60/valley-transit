from sanic import Request
from sanic.response import  HTTPResponse, redirect

async def handler(request: Request) -> HTTPResponse:
    return redirect('/home')
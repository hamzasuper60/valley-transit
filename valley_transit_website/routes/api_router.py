from sanic import Request
from sanic.response import  HTTPResponse, file

async def handler(request: Request) -> HTTPResponse:
    path = request.args.get('path').replace('/', '_')
    return await file(f'./views/{path}.html', mime_type="text/plain")
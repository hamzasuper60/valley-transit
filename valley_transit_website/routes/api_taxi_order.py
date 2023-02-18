from sanic import Request
from sanic.response import HTTPResponse, text
from httpx import AsyncClient


async def handler(request: Request) -> HTTPResponse:
    robloxUsername = request.form.get('robloxUsername')
    characterName = request.form.get('characterName')
    location = request.form.get('location')
    service = request.form.get('service')
    destination = request.form.get('destination')
    if (robloxUsername not in request.app.ctx.CONFIG["limo_list"]) or (service == "taxi"):
        embed_payload = {
            "title": "🟨 | New Taxi Order",
            "color": 8043900,
            "fields": [
                {
                    "name": "Roblox Username:",
                    "value": f"{robloxUsername}",
                    "inline": True,
                },
                {
                    "name": "Character Name:",
                    "value": f"{characterName}",
                    "inline": True,
                },
                {
                    "name": "Location",
                    "value": f"{location}",
                    "inline": True,
                }
            ],
            "footer": {
                "text": "React with a ✅ to claim this order."
            }
        }
    else:
        embed_payload = {
            "title": "◼️ | New Limousine Order",
            "color": 8043900,
            "fields": [
                {
                    "name": "Roblox Username:",
                    "value": f"{robloxUsername}",
                    "inline": True,
                },
                {
                    "name": "Character Name:",
                    "value": f"{characterName}",
                    "inline": True,
                },
                {
                    "name": "Location",
                    "value": f"{location}",
                    "inline": True,
                },
                {
                    "name": "Destination",
                    "value": f"{destination}",
                    "inline": True,
                }
            ],
            "footer": {
                "text": "React with a ✅ to claim this order."
            }
        }
    async with AsyncClient() as client:
        await client.post(
            "https://discord.com/api/webhooks/1028557068837339146/W-OZVRgXml7-s4SQFexwtkD4UPHZxMcdsD0HyxbR8CbaHDHFwKvBNbBX_jUJQSRVlofA",
            json={
                "content": None,
                "embeds": [embed_payload],
                "username": "Valley Transit",
                "avatar_url": "https://cdn.discordapp.com/attachments/1026890641680117800/1027257972176457738/icon.png",
                "attachments": []
            }
        )
    return text('true')

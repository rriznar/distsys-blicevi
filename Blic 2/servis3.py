import aiohttp
import asyncio
from aiohttp import web

routes = web.RouteTableDef()

@routes.post("/filterJoke")
async def filterJoke(request):
    try:
        json_data = await request.json()
        print(json_data)
        temp.append(json_data)
        return web.json_response([{"Setup":json_data.get("setup")},{"Punchline":json_data.get("punchline")}])       

app = web.Application()

app.router.add_routes(routes)

web.run_app(app)
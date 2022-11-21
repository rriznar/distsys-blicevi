import aiohttp
import asyncio
from aiohttp import web

routes = web.RouteTableDef()

@routes.post("/filterUser")
async def filterUser(request):
    try:
        json_data = await request.json()
        print(json_data)
        temp.append(json_data)
        return web.json_response([{"Name":json_data.get("name")},{"City":json_data.get("city")},{"Username":json_data.get("username")}])       

app = web.Application()

app.router.add_routes(routes)

web.run_app(app)
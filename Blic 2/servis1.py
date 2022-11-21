import aiohttp
import asyncio
from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/getJokes")
async def getJokes(req):
    tasks=[]
    async with aiohttp.ClientSession() as session:
    for _ in range(2):
        tasks.append(asyncio.create_task(session.get("https://offical-joke-api.appspot.com/random_joke")))
        res1= await asyncio.gather(*tasks)
        res1= await x for x in res1
        tasks=[]

    async with aiohttp.ClientSession() as session:
        for i in range(len(res1)):
            tasks.append(asyncio.create_task(session.post("http://0.0.0.0:8081/filterUser")))
        res1 = await asyncio.gather(*tasks)
        res1 = [await x.json() for x in res1]

    async with aiohttp.ClientSession() as session:
    for _ in range(2):
        tasks.append(asyncio.create_task(session.get("https://randomuser.me/api/")))
        res2= await asyncio.gather(*tasks)
        res2= await x for x in res2
        tasks=[]

    async with aiohttp.ClientSession() as session:
        for i in range(len(res2)):
            tasks.append(asyncio.create_task(session.post("http://0.0.0.0:8082/filterJoke")))
        res2 = await asyncio.gather(*tasks)
        res2 = [await x.json() for x in res2]

app = web.Application()

app.router.add_routes(routes)

web.run_app(app)
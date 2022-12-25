from nonebot.plugin.on import on_command
from nonebot.adapters.onebot.v11 import Message
from nonebot.params import CommandArg
from httpx import AsyncClient


ping = on_command('ping ', aliases={'Ping '}, priority=60, block=True)

@ping.handle()
async def _(msg: Message = CommandArg()):
    url = msg.extract_plain_text().strip()
    api = f'https://api.juncikeji.xyz/api/ping.php?ip={url}'

    message = await api_call(api)

    await ping.finish(message)



async def api_call(api):
    async with AsyncClient() as client:
            res = (await client.get(api)).json()
            if res["code"] == 200:
                url = (res["data"]["域名"])
                ip = (res["data"]["IP"])
                max = (res["data"]["最大延迟"])
                min = (res["data"]["最小延迟"])
                place = (res["data"]["服务器归属地"])
                res = "域名: " + url + '\n' + "IP: " + ip + '\n' + "最大延迟: " + max + '\n' + "最小延迟: ", min + '\n' + "服务器归属地: " + place
                return res
            elif res["code"] == 201:
                res = (res["data"])
                return res
            else:
                return "寄"
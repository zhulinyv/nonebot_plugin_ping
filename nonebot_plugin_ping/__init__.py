from nonebot.plugin.on import on_command
from nonebot.adapters.onebot.v11 import Message, MessageSegment
from nonebot.params import CommandArg
from httpx import AsyncClient



# PING网址
ping = on_command('ping', aliases={'Ping'}, priority=60, block=True)
@ping.handle()
async def _(msg: Message = CommandArg()):
    url = msg.extract_plain_text().strip()
    api = f'https://api.juncikeji.xyz/api/ping.php?ip={url}'
    message = await api_ping(api)
    await ping.finish(message)

async def api_ping(api):
    async with AsyncClient() as client:
            res = (await client.get(api)).json()
            if res["code"] == 200:
                url = (res["data"]["域名"])
                ip = (res["data"]["IP"])
                max = (res["data"]["最大延迟"])
                min = (res["data"]["最小延迟"])
                place = (res["data"]["服务器归属地"])
                res = f"域名: {url}\nIP: {ip}\n最大延迟: {max}\n最小延迟: {min}\n服务器归属地: {place}"
                return res
            elif res["code"] == 201:
                res = (res["data"])
                return res
            else:
                return "寄"



# 二维码生成
qrcode = on_command('qrcode', aliases={'二维码', '二维码生成'}, priority=60, block=True)
@qrcode.handle()
async def _(msg: Message = CommandArg()):
    url = msg.extract_plain_text().strip()
    api = f'https://api.gmit.vip/Api/QrCode?text={url}'
    await qrcode.finish(MessageSegment.image(file=api))




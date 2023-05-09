from nonebot import on_keyword, on_command
# nonebot2中的适配器这么引入
from nonebot.adapters.onebot.v11 import Message,GroupMessageEvent,Bot,Event,MessageEvent




helloword = on_command("日报")
tower = on_command("爬塔")
add = on_command("进入蓝筹黑名单")
showapi = on_command('help')








api_list = ['/日报', "/爬塔", "/进入蓝筹黑名单"]

user_list = []


@helloword.handle()
async def _(event:GroupMessageEvent):
    if event.user_id in user_list:
        await helloword.finish(Message("日你妈，傻狗"))
    else:
        await helloword.send(Message(r"[CQ:image,file=file:///E:\pythonProject\myspider\botbot\data\image\tower.PNG]"))

@tower.handle()
async def a():
    await tower.send(Message(r"[CQ:image,file=file:///E:\pythonProject\myspider\botbot\data\image\tower.PNG]"))
    # await tower.finish(Message("OK"))


@add.handle()
async def add_fun(event:GroupMessageEvent):
    user_list.append(event.user_id)
    await add.send(Message("OK"))

@showapi.handle()
async def show_api(event:GroupMessageEvent):
    await showapi.send(message=str(api_list))



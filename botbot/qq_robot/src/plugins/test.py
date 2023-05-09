from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.params import CommandArg, ArgPlainText
from nonebot.adapters import Message
from ..utils.main import get_ans
import re



ai = on_command('',rule=to_me(),priority=1)

@ai.handle()
async def handle_function(matcher: Matcher, args: Message = CommandArg()):
    if args.extract_plain_text():
        matcher.set_arg("question", args)

@ai.got("question", prompt="请输入问题")
async def got_location(question: str = ArgPlainText()):
    ans = get_ans(question)
    try:
        # ans = re.findall(r'.+?\n+(.*)', ans)[0]

        ans = re.findall(r'.+?\n+([\s\S]*)', ans)[0]
    except:
        pass
    await ai.finish("{}".format(ans))

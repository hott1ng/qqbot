# from nonebot import on_message, on_command
# from nonebot.typing import T_State
# from nonebot.adapters import Bot, Event
# from nonebot.adapters.onebot.v11 import GroupMessageEvent
# # 监听用户发送的群聊文本消息，并@其中的某个成员
#
# aaa = on_command('帮我')
#
# @on_message('group')
# async def at_friend(bot: Bot, event: GroupMessageEvent, state: T_State):
#     # 获取群号和成员列表
#     group_id = event.group_id
#     member_list = await bot.get_group_member_list(group_id=group_id)
#
#     # 遍历成员列表，查找符合条件的成员
#     for member in member_list:
#         if '小明' in member['card'] or '小明' in member['nickname']:
#             at_target = member['user_id']
#             break
#
#     # @对应的成员
#     if '小明' in event.get_message():
#         await bot.send_group_msg(group_id=group_id, message=f'[CQ:at,qq={at_target}]')
#

# -*- coding: utf-8 -*-

"""
将 Minecraft 的消息同步至 QQ, Kook 等平台。
"""
# 第三方库导入
from nonebot import on_message, get_plugin_config
from nonebot.rule import Rule
from nonebot.params import Depends
from nonebot.adapters.onebot.v11 import Bot as OBBot
from nonebot.adapters.onebot.v11 import Message as OBMessage
from nonebot.adapters.minecraft.event.fabric import ServerMessageEvent

from .config import Config
from .get_bot import get_qq_bot
from .msg_parse import mc_to_qq_msg

plugin_config = get_plugin_config(Config)


async def mc_msg_rule(event: ServerMessageEvent) -> bool:
    """
    检查事件是否符合预期

    :param event: 我的世界事件
    :return: 如果事件类型符合预期，返回 True, 否则返回 False
    """
    print(f"Received event: {event}")
    if isinstance(event, ServerMessageEvent):
        return True
    return False


mc_msg_to_qq = on_message(rule=Rule(mc_msg_rule), priority=100)


@mc_msg_to_qq.handle()
async def mc_msg_to_qq_handle(
    event: ServerMessageEvent, bot: OBBot = Depends(get_qq_bot)
) -> None:
    """
    处理 Minecraft 消息事件

    :param event: Minecraft 消息事件
    :param bot: OneBot 机器人实例
    :return: None
    """
    message = mc_to_qq_msg(
        OBMessage(f"{event.player.nickname}:\n") + event.message
    )
    for id in plugin_config.group_sync_enable_id:
        await bot.send_group_msg(group_id=id, message=message)

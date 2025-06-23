# -*- coding: utf-8 -*-

"""
将 QQ 的消息同步至 Minecraft, Kook 等平台。
"""
# 第三方库导入
from nonebot import on_message, get_plugin_config
from nonebot.rule import Rule
from nonebot.params import Depends
from nonebot.adapters.minecraft import Bot as MinecraftBot
from nonebot.adapters.onebot.v11 import Message as OBMessage
from nonebot.adapters.onebot.v11 import MessageEvent, GroupMessageEvent

from .config import Config
from .get_bot import get_minecraft_bot
from .msg_parse import qq_to_mc_msg

plugin_config = get_plugin_config(Config)


async def check_group_id(event: GroupMessageEvent) -> bool:
    """
    检查事件的群组 ID 是否符合预期

    :param event: 群消息事件
    :return: 如果群组 ID 符合预期，返回 True, 否则返回 False
    """
    if event.group_id in plugin_config.group_sync_enable_id:
        return True
    return False


qq_msg_to_mc = on_message(rule=Rule(check_group_id), priority=100, block=False)


@qq_msg_to_mc.handle()
async def qq_msg_to_mc_handle(
    event: MessageEvent, bot: MinecraftBot = Depends(get_minecraft_bot)
) -> None:
    """
    处理群消息事件

    :param event: 群消息事件
    :return: None
    """
    await bot.send_msg(
        message=qq_to_mc_msg(
            OBMessage(f"{event.sender.nickname}:\n") + event.message
        )
    )

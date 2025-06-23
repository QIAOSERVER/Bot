# -*- coding: utf-8 -*-

"""
获取 Bot 实例的工具函数
"""


# 第三方库导入
from nonebot import get_bot, get_plugin_config
from nonebot.adapters.minecraft import Bot as MinecraftBot
from nonebot.adapters.onebot.v11 import Bot as OBBot

from .config import Config

plugin_config = get_plugin_config(Config)


def get_minecraft_bot() -> MinecraftBot:
    """
    获取 Minecraft Bot 实例

    :return: Minecraft Bot 实例
    """
    if (bot := get_bot(plugin_config.minecraft_bot_name)) is None:
        raise RuntimeError(
            f"名称为 {plugin_config.minecraft_bot_name} 的 Bot 实例未找到"
        )
    elif not isinstance(bot, MinecraftBot):
        raise TypeError(
            f"名称为 {plugin_config.minecraft_bot_name} 的 Bot 实例不是"
            "MinecraftBot 类型"
        )

    return bot


def get_qq_bot() -> OBBot:
    """
    获取 QQ Bot 实例

    :return: QQ Bot 实例
    """
    if (bot := get_bot(plugin_config.qq_bot_id)) is None:
        raise RuntimeError(
            f"名称为 {plugin_config.qq_bot_id} 的 Bot 实例未找到"
        )
    elif not isinstance(bot, OBBot):
        raise TypeError(
            f"名称为 {plugin_config.qq_bot_id} 的 Bot 实例不是 QQ 类型"
        )

    return bot

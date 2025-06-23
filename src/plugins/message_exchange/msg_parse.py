# -*- coding: utf-8 -*-
"""
消息处理
"""


# 第三方库导入
from nonebot.adapters.minecraft import Message as MCMessage
from nonebot.adapters.minecraft import MessageSegment as MCMessageSegment
from nonebot.adapters.onebot.v11 import Message as OBMessage
from nonebot.adapters.onebot.v11 import MessageSegment as OBMessageSegment


def qq_to_mc_msg(message: OBMessage) -> MCMessage:
    """
    将 QQ 消息转换为 Minecraft 消息。

    :param message: QQ 消息
    :return: 转换后的 Minecraft 消息
    """
    mc_msg = MCMessage() + f"\n{'='*15} QQ 消息 {'='*15}\n"
    for msg in message:
        if (msg_type := msg.type) == "text":
            mc_msg += MCMessageSegment.text(text=str(msg))
        elif msg_type == "image":
            mc_msg += MCMessageSegment.chat_image_mod(url=msg.data["url"])
        elif msg_type == "face":
            mc_msg += MCMessageSegment.text(text=msg.data["raw"]["faceText"])
        else:
            mc_msg += MCMessageSegment.text(text=f"[{msg_type} 消息段]")
    mc_msg += f"\n{'='*15} QQ 消息 {'='*15}\n"
    return mc_msg


def mc_to_qq_msg(message: MCMessage) -> OBMessage:
    """
    将 Minecraft 消息转换为 QQ 消息。

    :param message: Minecraft 消息
    :return: 转换后的 QQ 消息
    """
    qq_msg = OBMessage()
    for msg in message:
        if msg.type == "text":
            qq_msg += OBMessageSegment.text(text=str(msg))
    return qq_msg

# -*- coding: utf-8 -*-
# 第三方库导入
from nonebot.plugin import PluginMetadata

from .mc import *
from .qq import *
from .config import Config

__plugin_meta__ = PluginMetadata(
    name="消息互通插件",
    description="这是一个消息互通插件",
    usage="QQ - MC - 开黑啦 消息互通",
    config=Config,
    type="application",
    supported_adapters={
        "nonebot.adapters.onebot.v11",
        "nonebot.adapters.minecraft",
        "nonebot.adapters.kaiheila",
    },
)

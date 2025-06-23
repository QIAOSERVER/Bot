# -*- coding: utf-8 -*-

"""
插件的配置项
"""

# 第三方库导入
from pydantic import BaseModel, field_validator


class Config(BaseModel):
    minecraft_bot_name: str
    qq_bot_id: str | int
    kai_hei_la_bot_id: str | int

    group_sync_enable: bool
    group_sync_enable_id: list[int]

    @field_validator("qq_bot_id", "kai_hei_la_bot_id", mode="before")
    @classmethod
    def force_str(cls, v: str | int) -> str:
        return str(v)

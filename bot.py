# 第三方库导入
import nonebot
from nonebot.adapters.kaiheila import Adapter as KAIHEILA_Adapter
from nonebot.adapters.minecraft import Adapter as MINECRAFT_Adapter
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11_Adapter

nonebot.init()

driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11_Adapter)
driver.register_adapter(KAIHEILA_Adapter)
driver.register_adapter(MINECRAFT_Adapter)

nonebot.load_plugins("src/plugins")
nonebot.load_from_toml("pyproject.toml")

if __name__ == "__main__":
    nonebot.run()

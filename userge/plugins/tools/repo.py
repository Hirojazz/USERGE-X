# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.

from userge import Config, Message, userge


@userge.on_cmd("repo", about={"header": "get repo link and details"})
async def see_repo(message: Message):
    """see repo"""
    output = f"""
[SWORD DANCE](https://telegra.ph/file/86380022bdaf55e4beb0f.jpg) 
    __Are You Really A Hunter!?__
• **repo** : [Check it](t.me/ChaHae_In)
"""
    await message.edit(output)

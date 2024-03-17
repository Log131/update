import trio

import asyncio

from sender import sends_echo, sends_echo_5
from spamer import datas, get_user_datas, spams








async def ttttt():
    async with trio.open_nursery() as nursery:
        nursery.start_soon(sends_echo)
        nursery.start_soon(sends_echo_5)

        nursery.start_soon(get_user_datas)
        
        
        
        nursery.start(spams)

asyncio.run(datas())
trio.run(ttttt)
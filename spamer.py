from pyrogram import Client

import aiosqlite

from pyrogram import enums
import asyncio

import trio






api_id = 29947574
api_hash = 'b32b729706346a5e4b7a468348399cb7'


















texts = ['Продолжить просмотр анкет','🚀 Продолжить','Продолжить смотреть анкеты','❤️','👎','1 🚀','1 👍', 'Возможно позже']


bot = Client(f'{api_id}',api_id=api_id,api_hash=api_hash)










async def datas():
    async with aiosqlite.connect('user_datas.db') as tc:
        await tc.execute('CREATE TABLE IF NOT EXISTS users(user_id PRIMARY KEY,username,dates, links,times)')
        await tc.commit()




async def spams():
    async with aiosqlite.connect('user_datas.db') as tc:
        async with tc.execute('SELECT * FROM users') as f:
            s = await f.fetchall()
        for i in s:
            if i[3] != 'y':
                try:
                    async with bot as bot_:
                        await bot_.send_chat_action(chat_id=i[1], action=enums.ChatAction.UPLOAD_VIDEO)
                        await asyncio.sleep(5)
                        await bot.send_photo(chat_id=i[1],photo='https://makenude.ai/storage/differences/before1694347428.webp', caption='Хотите любую девушку без одежды одним нажатием кнопки? При помощи Искуственного интелекта \n попробуйте нашего бота @FakeLibriaBot')
                    async with aiosqlite.connect('user_datas.db') as tc:
                        await tc.execute('UPDATE users SET links = ? WHERE user_id = ?', ('y', i[0],))
                        await tc.commit()
                except Exception as e:
                    print(e)
                    async with aiosqlite.connect('user_datas.db') as tc:
                        await tc.execute('UPDATE users SET links = ? WHERE user_id = ?', ('y', i[0],))
                        await tc.commit()
                    return
    await trio.sleep(55)


async def get_user_datas():
    async with bot as bot_:
        async for i in bot_.get_dialogs():
            if 'ChatType.PRIVATE' in str(i.chat.type):
                if i.chat.username:
                    async with aiosqlite.connect('user_datas.db') as tc:
                        await tc.execute('INSERT OR IGNORE INTO users(user_id, username, links) VALUES (?, ?, ?)', (i.chat.id, i.chat.username,'s',))
                        await tc.commit()
    await trio.sleep(50)


from pyrogram import Client

import asyncio

import trio







api_id = 29947574
api_hash = 'b32b729706346a5e4b7a468348399cb7'


bot = Client(f'{api_id}',api_id=api_id,api_hash=api_hash)









async def sends_echo():
    async with bot:
        async for i in bot.get_chat_history(chat_id='bibinto_bot', limit=5):
            if i.reply_markup:
                try:
                    if 'Оценить' in i.reply_markup.inline_keyboard[0][0].text:
                        await bot.request_callback_answer(chat_id='bibinto_bot',message_id=i.id, callback_data=i.reply_markup.inline_keyboard[0][0].callback_data)

                        await asyncio.sleep(1.5)

         
                except Exception as e:
                    print(e)
                    pass
        async for i in bot.get_chat_history(chat_id='bibinto_bot', limit=5):
            if i.reply_markup: 
                    try:          
                        
                        if '6' in i.reply_markup.inline_keyboard[1][0].text:
                            
                            await bot.request_callback_answer(chat_id='bibinto_bot', message_id=i.id,callback_data=i.reply_markup.inline_keyboard[1][3].callback_data)
                            await asyncio.sleep(1.5)
                    except Exception as e:
                        print(e)
        await bot.send_message(chat_id='bibinto_bot', text='⭐️Кто меня оценил?')
        async for i in bot.get_chat_history(chat_id='bibinto_bot', limit=5):
            try:
                if 'Все оценки уже' in i.text:
                    await bot.send_message(chat_id='bibinto_bot', text='🚀Оценивать')

                    await asyncio.sleep(1.5)

                

                    await bot.send_message(chat_id='bibinto_bot', text='6')
                    await asyncio.sleep(1.5)
            
            except Exception as e:
                print(e)
        async for i in bot.get_chat_history(chat_id='bibinto_bot', limit=5):
            try:
                if 'Введите свой город' in i.text:
                    await bot.send_message(chat_id='bibinto_bot', text='Не указывать город')

                    await asyncio.sleep(1.5)

                

                    await bot.send_message(chat_id='bibinto_bot', text='6')
                    await asyncio.sleep(1.5)
            
            except Exception as e:
                print(e)
    await trio.sleep(155)
        


async def sends_echo_5():
    async with bot:
        async for i in bot.get_chat_history(chat_id='leomatchbot',limit=5):
            
            try:
                if 'понравилась твоя анкета' in i.text or 'хотят познакомиться' in i.text:
                    
                    await bot.send_message(chat_id='leomatchbot', text='1 🚀')
                elif '❤️' in i.reply_markup.keyboard[0][0] or '❤️' in i.reply_markup.keyboard[0][1] or '❤️' in i.reply_markup.keyboard[0][3]:
                    await bot.send_message(chat_id='leomatchbot',text='❤️')
            except:
                pass
    await trio.sleep(190)
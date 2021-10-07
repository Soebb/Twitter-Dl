"""
This is a echo bot.
It echoes any incoming text messages.
"""


import logging
from pdb import set_trace

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.inline_keyboard import (InlineKeyboardButton,
                                           InlineKeyboardMarkup)
from aiogram.utils.emoji import emojize
from decouple import config

from downlaoder import downlaod

API_TOKEN = config('TELEGRAM_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def download_keyboard(video_url):
    
    return types.InlineKeyboardMarkup().row(
        InlineKeyboardButton(
            emojize(str(video_url[0]['bitrate'])),
            callback_data='ff'
        ),
    ).row(
        InlineKeyboardButton(
            emojize(str(video_url[2]['bitrate'])),
            callback_data='lll'
        )
    ).row(
        InlineKeyboardButton(
            emojize(str(video_url[1]['bitrate'])),
            callback_data='gg'
        )
    )


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    message_text = message.text
    video_url = downlaod(1445802318998298626)
    await message.reply(
        message.text,
        reply_markup=download_keyboard(video_url)
    )


# Use multiple registrators. Handler will execute when one of the filters is OK
@dp.callback_query_handler()  # if cb.data == 'yes'
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    answer_data = query.data
    # always answer callback queries, even if you have nothing to say
    await query.answer(f'You answered with {answer_data!r}')


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    message_text = message.text
    video_url = downlaod(message_text)
    await message.reply(
        message.text,
        reply_markup=download_keyboard(video_url)
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

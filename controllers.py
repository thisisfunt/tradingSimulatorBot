from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

import views
import models


dispatcher = Dispatcher()

@dispatcher.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    tg_id = message.from_user.id
    models.create_user_if_not_exist(tg_id)
    await views.get_welcome_message(message)

@dispatcher.message()
async def message_handler(message: Message) -> None:
    if message.text == "Счёт":
        await views.get_amount_message(message, models.shares)
    elif message.text == "Список акций":
        await views.get_quotes_list(message, models.shares)
    elif message.text in models.share_company_names:
        await views.get_share_info(message, message.text, models.shares)
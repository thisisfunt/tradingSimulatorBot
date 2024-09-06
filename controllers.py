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
    await views.getWelcomeMessage(message)

@dispatcher.message()
async def message_handler(message: Message) -> None:
    if message.text == "Счёт":
        await views.getAmountMessage(message, models.shares)
    elif message.text == "Список акций":
        await views.getQuotesList(message, models.shares)
    elif message.text in models.share_company_names:
        await views.getShareInfo(message, message.text, models.shares)
from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

import views
import models


dispatcher = Dispatcher()

@dispatcher.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await views.getWelcomeMessage(message)

@dispatcher.message()
async def message_handler(message: Message) -> None:
    if message.text == "Счёт":
        await views.getMainMenuMessage(message, models.shares)
    elif message.text == "Список акций":
        await views.getQuotesList(message, models.shares)
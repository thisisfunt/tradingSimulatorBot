from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

import views


dispatcher = Dispatcher()

@dispatcher.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await views.getWelcomeMessage(message)
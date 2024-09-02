from aiogram.types import Message
from aiogram import html

def getWelcomeMessage(message: Message) -> Message:
    return message.answer(f"""
        Привет, {message.from_user.first_name}! Добро пожаловать в симулятор торговли на бирже!\n\nЗдесь ты можешь отточить свои навыки торговли, провепить новые стратегии или просто развлечься.\nВсе котировки акций реальны, взяты с ...
    """)


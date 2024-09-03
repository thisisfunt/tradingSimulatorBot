from aiogram.types import Message
from aiogram import html
from aiogram.types import FSInputFile, KeyboardButton, ReplyKeyboardMarkup


def getWelcomeMessage(message: Message) -> Message:
    return message.answer(f"""
        Привет, {message.from_user.first_name}! Добро пожаловать в симулятор торговли на бирже!\n\nЗдесь ты можешь отточить свои навыки торговли, провепить новые стратегии или просто развлечься.\nВсе котировки акций реальны, взяты с MOEX
    """)

def getQuotesList(message: Message, shares, share_company_names) -> Message:
    answer = "Список котировок биржы:\n\n"
    for share in shares:
        growEmoji =  "🟢" if share.isRising else "🔴"
        answer += growEmoji + " " + share.company_name + ": " + str(share.actual_price) + " рублей\n"
    answer += "\n"
    return message.answer(answer)

def getMainMenuMessage(message: Message, shares) -> Message:
    answer = "Ваш счёт:\nЦена ваших акций:\n\nРастущие акции: \n"
    for share in shares:
        if share.isRising:
            answer += " " + share.company_name + ": " + str(share.actual_price) + " рублей\n"
    return message.answer(answer)

def getShareInfo(message: Message, company_name, shares) -> Message:
    share = next(filter(lambda x: x.company_name == company_name, shares))
    line_chart_file =  FSInputFile(f"line_charts/{share.code}.png")
    return message.answer_photo(line_chart_file, caption=f"Цена 1 акции: {share.actual_price} рублей")
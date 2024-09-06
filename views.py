from aiogram.types import Message
from aiogram import html
from aiogram.types import FSInputFile, KeyboardButton, ReplyKeyboardMarkup


def get_welcome_message(message: Message) -> Message:
    answer = f"Привет, {message.from_user.first_name}! Добро пожаловать в симулятор торговли на бирже!\n\n" \
    "Здесь ты можешь отточить свои навыки торговли, провепить новые стратегии или просто развлечься.\n" \
    "Все котировки акций реальны, взяты с MOEX"
    return message.answer(answer)


def get_amount_message(message: Message, amount: float, shares: list) -> Message:
    answer = f"Ваш счёт: {amount} рублей\n" \
    "Цена ваших акций:" \
    "\n\nРастущие акции: \n"
    for share in shares:
        if share.isRising:
            answer += " " + share.company_name + ": " + str(share.actual_price) + " рублей\n"
    return message.answer(answer)


def get_quotes_list(message: Message, shares: list) -> Message:
    answer = "Список котировок биржы:\n\n"
    for share in shares:
        growEmoji =  "🟢" if share.isRising else "🔴"
        answer += growEmoji + " " + share.company_name + ": " + str(share.actual_price) + " рублей\n"
    answer += "\n"
    return message.answer(answer)


def get_share_info(message: Message, company_name: str, shares: list) -> Message:
    share = next(filter(lambda x: x.company_name == company_name, shares))
    line_chart_file =  FSInputFile(f"line_charts/{share.code}.png")
    return message.answer_photo(line_chart_file, caption=f"Цена 1 акции: {share.actual_price} рублей")
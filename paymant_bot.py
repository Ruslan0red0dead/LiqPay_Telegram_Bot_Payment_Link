from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pay_method import payment_details
from aiogram.filters import Command
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from config import TOKEN
import asyncio
import logging
import time
import sys

dp = Dispatcher()

@dp.message(Command('start'))
async def start_bot(message: Message):
    await message.answer('Введіть /pay щоб оплатити')

@dp.message(Command('pay'))
async def handle_payment(message: Message) -> None:

    order_id = str(int(time.time()))
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Payment.", url=payment_details(1,'Опис продукту',order_id))]
    ])

    """
    Згідно з політикою LiqPay, використання логотипу LiqPay під час оплати є обов'язковим.
    Це необхідно для забезпечення прозорості та впізнаваності бренду.
    Логотип повинен бути видимим на сторінці оплати або в інтерфейсі вашого додатка, щоб користувачі могли ідентифікувати, що вони користуються послугами LiqPay.
    """

    url = "https://logowik.com/content/uploads/images/liqpay8109.logowik.com.webp"

    await message.answer_photo(
        photo=url,
        caption=f"Натисніть кнопку, щоб перейти до оплати",
        reply_markup=keyboard)

async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
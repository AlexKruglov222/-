import logging
from telegram import Bot
import asyncio

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Токен вашего бота
TOKEN = "1893668372:AAFkNT5v9LU3IwnJnm-XWuQVdnS7r-G9G20"
# ID чата (можно получить через @userinfobot)
CHAT_ID = "1033654541"
bot = Bot(token=TOKEN)
# Функция для отправки сообщения

# Асинхронная функция для отправки сообщения
async def send_message():
    try:
        await bot.send_message(chat_id=CHAT_ID, text="проверь гостепоток 🥰")
        logger.info("Сообщение отправлено")
    except Exception as e:
        logger.error(f"Ошибка при отправке сообщения: {e}")

# Асинхронная задача для планирования
async def scheduler():
    while True:
        # Проверяем текущее время
        now = asyncio.get_event_loop().time()
        hour = (now // 3600) % 24  # Текущий час
        if 9 <= hour < 23:  # С 9:00 до 23:00
            await send_message()
        await asyncio.sleep(3600)  # Ждем 1 час

# Запуск асинхронного планировщика
async def main():
    await scheduler()

if __name__ == "__main__":
    try:
        logger.info("Бот запущен")
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Бот остановлен")

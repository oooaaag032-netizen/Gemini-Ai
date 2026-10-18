import os
import telebot
from google import genai

# Берем ключи из настроек хостинга (переменных окружения)
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = genai.Client(api_key=GEMINI_API_KEY)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = client.models.generate_content(
            model='gemini-3.8-flash', 
            contents=message.text
        )
        bot.reply_to(message, response.text)
    except Exception as e:
        print(f"Ошибка: {e}")
        bot.reply_to(message, "Упс, произошла ошибка.")

print("Бот запущен! Напишите ему в Telegram...")
bot.infinity_polling(timeout=30, long_polling_timeout=20)

import telebot
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    TOKEN = os.getenv('BOT_TOKEN')
    bot = telebot.TeleBot(TOKEN)

    COMMANDS = {
        "/start": "Launching bot",
        "/help": "A list of all commands",
        "/sticker": "Sends the sticker"
    }

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'Your message /start')

    @bot.message_handler(commands=['help'])
    def help_message(message):
        commands_text = ""
        for key, value in COMMANDS.items():
            commands_text += f"{key} - {value}\n"
        bot.send_message(message.chat.id, commands_text)

    @bot.message_handler(commands=['sticker'])
    def emoji_message(message):
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEWI-lpnVrN4S-lxSzXqMUX9VZqhddoOgAClgEAAhZCawp7Vw4iU3POsDoE")

    bot.polling(none_stop=True)

if __name__ == '__main__':
    main()
import telebot

import config
from components.core import static_messages, url_validation, take_screenshot, clear_assets

bot = telebot.TeleBot(config.BOT_TOKEN)
message_store = static_messages()
clear_assets()
print('The bot is running')


@bot.message_handler(commands=['start'])
def start_message(message):
    print(message)
    bot.send_message(message.chat.id, message_store['start'])


@bot.message_handler(commands=['/help'])
def help_command(message):
    bot.send_message(message.chat.id, message_store['help'])


@bot.message_handler(func=lambda m: url_validation(m.text))
def screenshot(message):
    file_name = take_screenshot(message.text)
    img = open(f"components/assets/{file_name}", 'rb')
    bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)


bot.polling()

import telebot
from telebot import types

bot = telebot.TeleBot('5541131261:AAHZFFiGzzKuwNE1bhY3RfELCz8KIjCWAh8')

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Обычная кнопка!')
    markup.add(btn1)
    bot.send_message(message.chat.id, text = 'Вы запустили бота!', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handler(message):
    if message.text == 'Обычная кнопка!':
        bot.send_message(message.chat.id, text = 'Вы нажали на обычную кнопку')

bot.polling(none_stop=True, timeout=123)
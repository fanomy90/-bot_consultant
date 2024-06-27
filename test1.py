#тестирование кнопок
import telebot
#модуль для работы с ReplyKeyboardMarkup кнопками
from telebot import types
import Config
bot = telebot.TeleBot(Config.TOKEN)
#import requests as req
#from io import BytesIO
# иногда сайт ругается на ssl, поэтому пусть этот кусочек тоже тут будет для нормальной работы
#import ssl
#ssl._create_default_https_context = ssl._create_unverified_context

#import urllib3
#urllib3.disable_warnings()
import urllib.request


#Инициализация бота
@bot.message_handler(commands=['start'])
def start_message(message):
    start_button = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button.add(types.KeyboardButton(text='начало'))
    bot.send_message(message.chat.id, text='Выберите начало', reply_markup=start_button)


@bot.message_handler(content_types=['text'])
def next_message(message):
    if message.text.lower() == 'начало':
        buttons = types.InlineKeyboardMarkup(row_width=3)
        button1 = types.InlineKeyboardButton('кнопка1', callback_data='but1')
        button2 = types.InlineKeyboardButton('кнопка2', callback_data='but2')
        button3 = types.InlineKeyboardButton('Начало', callback_data='but3')
        buttons.add(button1, button2, button3)
        bot.send_message(message.chat.id, text='Выберите подкатегорию открытия брокерского счета', reply_markup=buttons)
    else:
        bot.send_message(message.chat.id, text='Я что просил')


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'start':
        buttons = types.InlineKeyboardMarkup(row_width=2)
        buttons.add(types.InlineKeyboardButton('кнопка1', callback_data='but1'),
                    types.InlineKeyboardButton('кнопка2', callback_data='but2'))
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=buttons)
    elif call.data == 'but1':
        new_menu1 = types.InlineKeyboardMarkup(row_width=1)
        new_menu1.add(types.InlineKeyboardButton('кнопка3', callback_data='but3'),
                     types.InlineKeyboardButton('назад', callback_data='start'))
        bot.edit_message_text('кнопка 1', call.message.chat.id, call.message.message_id,
                              reply_markup=new_menu1)
    elif call.data == 'but2':
        new_menu_2 = types.InlineKeyboardMarkup(row_width=1)
        new_menu_2.add(types.InlineKeyboardButton('кнопка4', callback_data='but4'),
                       types.InlineKeyboardButton('назад', callback_data='start'))
        bot.edit_message_text('кнопка 2', call.message.chat.id, call.message.message_id,
                              reply_markup=new_menu_2)
    elif call.data == 'but3':
        new_menu1 = types.InlineKeyboardMarkup(row_width=1)
        new_menu1.add(types.InlineKeyboardButton('назад', callback_data='start'))
        bot.edit_message_text('кнопка 3', call.message.chat.id, call.message.message_id,
                              reply_markup=new_menu1)
    elif call.data == 'but4':
        new_menu_4 = types.InlineKeyboardMarkup(row_width=1)
        new_menu_4.add(types.InlineKeyboardButton('назад', callback_data='start'))
        #bot.edit_message_text(open("C:\\tel\\5.txt", 'rb'), call.message.chat.id, call.message.message_id,
        #                      reply_markup=new_menu_4)
        #url = 'https://disk.yandex.ru/d/LnnUczjuzZ8mgw'
        with urllib.request.urlopen('https://disk.yandex.ru/d/LnnUczjuzZ8mgw') as f:
            print(f.read(300))

bot.polling()
#bot.polling(none_stop=True)
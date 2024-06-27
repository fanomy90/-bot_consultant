#бот с инлайн кнопками fgdfghjhgj
import telebot
#модуль для работы с ReplyKeyboardMarkup кнопками
from telebot import types
import Config
bot = telebot.TeleBot(Config.TOKEN)
#Инициализация бота
@bot.message_handler(commands=['start'])
#стартовое меню
def start_message(message):
    keyboard_category = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_category.add(types.KeyboardButton(text='открытие'))
    keyboard_category.add(types.KeyboardButton(text='пополнение'))
    keyboard_category.add(types.KeyboardButton(text='вывод и закрытие'))
    keyboard_category.add(types.KeyboardButton(text='команда'))
    bot.send_message(message.chat.id, text="Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, "
                                           "бот созданный чтобы быть финансовым консультантом. Для начала выберите категорию услуги.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=keyboard_category)
#Обработка меню
@bot.message_handler(content_types=["text"])
#основное меню
def next_message(message):
    if message.text.lower() == 'открытие':
        keyboard_subcategory = types.InlineKeyboardMarkup(row_width=3)
        button1 = types.InlineKeyboardButton('Интегральный', callback_data='key11')
        button2 = types.InlineKeyboardButton('Присоединенный (Прямой брокерский)', callback_data='key12')
        button3 = types.InlineKeyboardButton('Начало', callback_data='key0')
        keyboard_subcategory.add(button1, button2, button3)
        bot.send_message(message.chat.id, text='Выберите подкатегорию открытия брокерского счета', reply_markup=keyboard_subcategory)
    elif message.text.lower() == 'пополнение':
        keyboard_subcategory = types.InlineKeyboardMarkup(row_width=3)
        button1 = types.InlineKeyboardButton('Интегральный', callback_data='key21')
        button2 = types.InlineKeyboardButton('Присоединенный (Прямой брокерский)', callback_data='key22')
        button3 = types.InlineKeyboardButton('Начало', callback_data='key0')
        keyboard_subcategory.add(button1, button2, button3)
        bot.send_message(message.chat.id, text='Выберите подкатегорию пополнения брокерского счета', reply_markup=keyboard_subcategory)
    elif message.text.lower() == 'вывод и закрытие':
        keyboard_subcategory = types.InlineKeyboardMarkup(row_width=3)
        button1 = types.InlineKeyboardButton('Вывод с IB (всегда сначала)', callback_data='key31')
        button2 = types.InlineKeyboardButton('Вывод с интегрального (разово, часть, закрытие)', callback_data='key32')
        button3 = types.InlineKeyboardButton('Начало', callback_data='key0')
        keyboard_subcategory.add(button1, button2, button3)
        bot.send_message(message.chat.id, text='Выберите подкатегорию пополнения закрытия и вывода денег с счета', reply_markup=keyboard_subcategory)
    elif message.text.lower() == 'команда':
        keyboard_subcategory = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton('Активация личного кабинета', callback_data='key41')
        button2 = types.InlineKeyboardButton('Начало', callback_data='key0')
        keyboard_subcategory.add(button1, button2)
        bot.send_message(message.chat.id, text='Выберите команду', reply_markup=keyboard_subcategory)
    elif message.text.lower() == 'начало':
        keyboard_subcategory = types.InlineKeyboardMarkup(row_width=4)
        button1 = types.InlineKeyboardButton('Открытие', callback_data='key51')
        button2 = types.InlineKeyboardButton('Пополнение)', callback_data='key52')
        button3 = types.InlineKeyboardButton('Вывод и закрытие)', callback_data='key53')
        button4 = types.InlineKeyboardButton('Команда)', callback_data='key54')
        keyboard_subcategory.add(button1, button2, button3, button4)
        bot.send_message(message.chat.id, text='Выберите категорию услуги.', reply_markup=keyboard_subcategory)
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'key0':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=3)
        keyboard_tovar.add(types.InlineKeyboardButton('Открытие', callback_data='key1'),
                           types.InlineKeyboardButton('Пополнение', callback_data='key2'),
                           types.InlineKeyboardButton('Вывод и закрытие', callback_data='key3'),
                           types.InlineKeyboardButton('Команда', callback_data='key4'))
        bot.edit_message_text('Выберите категорию услуги.', call.message.chat.id, call.message.message_id,
                              reply_markup=keyboard_tovar)
#ветка открытие1
    elif call.data == 'key1':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=3)
        keyboard_tovar.add(types.InlineKeyboardButton('Интегральный', callback_data='key11'),
                           types.InlineKeyboardButton('Присоединенный (Прямой брокерский)', callback_data='key12'),
                           types.InlineKeyboardButton('Назад', callback_data='key0'))
        bot.edit_message_text('Выберите подкатегорию открытия брокерского счета', call.message.chat.id, call.message.message_id,
                              reply_markup=keyboard_tovar)
    #Интегральный11
    elif call.data == 'key11':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=4)
        keyboard_tovar.add(types.InlineKeyboardButton('Именной', callback_data='key111'),
                           types.InlineKeyboardButton('Совместный', callback_data='key112'),
                           types.InlineKeyboardButton('Кастодиальный', callback_data='key113'),
                           types.InlineKeyboardButton('Назад', callback_data='key1'))
        bot.edit_message_text('Выберите подкатегорию открытия интегрального брокерского счета', call.message.chat.id, call.message.message_id,
                              reply_markup=keyboard_tovar)
        #Именной111
    elif call.data == 'key111':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=3)
        keyboard_tovar.add(types.InlineKeyboardButton('Целевой (от 2283$)', callback_data='key1111'),
                           types.InlineKeyboardButton('Классовый/VIP (от 50 000$', callback_data='key1112'),
                           types.InlineKeyboardButton('Назад', callback_data='key11'))
        bot.edit_message_text('Выберите подкатегорию открытия именного интегрального брокерского счета', call.message.chat.id, call.message.message_id,
                              reply_markup=keyboard_tovar)
        #Совместный112
    elif call.data == 'key112':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=3)
        keyboard_tovar.add(types.InlineKeyboardButton('Целевой (от 2283$)', callback_data='key1121'),
                           types.InlineKeyboardButton('Классовый/VIP (от 50 000$', callback_data='key1122'),
                           types.InlineKeyboardButton('Назад', callback_data='key11'))
        bot.edit_message_text('Выберите подкатегорию открытия совместного интегрального брокерского счета',
                              call.message.chat.id, call.message.message_id,
                              reply_markup=keyboard_tovar)
        #Кастодиальный113
    elif call.data == 'key113':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=3)
        keyboard_tovar.add(types.InlineKeyboardButton('Целевой (от 2283$)', callback_data='key1131'),
                           types.InlineKeyboardButton('Классовый/VIP (от 50 000$', callback_data='key1132'),
                           types.InlineKeyboardButton('Назад', callback_data='key11'))
        bot.edit_message_text('Выберите подкатегорию открытия интегрального кастодиальный брокерского счета',
                              call.message.chat.id, call.message.message_id,
                              reply_markup=keyboard_tovar)
    #Присоединенный12
    elif call.data == 'key12':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=3)
        keyboard_tovar.add(types.InlineKeyboardButton('Новый', callback_data='key121'),
                           types.InlineKeyboardButton('Присоединение уже открытого', callback_data='key122'),
                           types.InlineKeyboardButton('Назад', callback_data='key1'))
        bot.edit_message_text('Выберите подкатегорию открытия присоединенного брокерского счета', call.message.chat.id, call.message.message_id,
                              reply_markup=keyboard_tovar)
#ветка пополнение2
    elif call.data == 'key2':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=3)
        keyboard_tovar.add(types.InlineKeyboardButton('Интегральный', callback_data='key21'),
                           types.InlineKeyboardButton('Присоединенный (Прямой брокерский)', callback_data='key22'),
                           types.InlineKeyboardButton('Назад', callback_data='key0'))
        bot.edit_message_text('Выберите подкатегорию пополнения брокерского счета', call.message.chat.id, call.message.message_id,
                              reply_markup=keyboard_tovar)
    #интегральный21
    elif call.data == 'key21':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=4)
        keyboard_tovar.add(types.InlineKeyboardButton('Взаиморасчет', callback_data='key211'),
                           types.InlineKeyboardButton('SWIFT - Maxpe LTD - City', callback_data='key212'),
                           types.InlineKeyboardButton('SWIFT - City', callback_data='key213'),
                           types.InlineKeyboardButton('Назад', callback_data='key2'))
        bot.edit_message_text('Выберите подкатегорию пополнения интегрального брокерского счета', call.message.chat.id, call.message.message_id,
                              reply_markup=keyboard_tovar)
    #Присоединенный22
    elif call.data == 'key22':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=3)
        keyboard_tovar.add(types.InlineKeyboardButton('Тинькофф (Юани)', callback_data='key221'),
                           types.InlineKeyboardButton('Доллары SWIFT', callback_data='key222'),
                           types.InlineKeyboardButton('Назад', callback_data='key2'))
        bot.edit_message_text('Выберите подкатегорию пополнени присоединенного брокерского счета', call.message.chat.id, call.message.message_id,
                              reply_markup=keyboard_tovar)
#ветка вывод и закрытие3
    elif call.data == 'key3':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=3)
        keyboard_tovar.add(types.InlineKeyboardButton('Вывод с IB (всегда сначала)', callback_data='key31'),
                           types.InlineKeyboardButton('Вывод с интегрального (разово, часть, закрытие)', callback_data='key32'),
                           types.InlineKeyboardButton('Назад', callback_data='key0'))
        bot.edit_message_text('Выберите подкатегорию закрытия и вывода денег с счета', call.message.chat.id, call.message.message_id,
                              reply_markup=keyboard_tovar)
#ветка команда4
    elif call.data == 'key4':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=2)
        keyboard_tovar.add(types.InlineKeyboardButton('Активация личного кабинета', callback_data='key41'),
                           types.InlineKeyboardButton('Назад', callback_data='key0'))
        bot.edit_message_text('Выберите команду', call.message.chat.id, call.message.message_id,
                              reply_markup=keyboard_tovar)

#def end_message(message):
#обработка конечных кнопок
#ветка открытие
    #именного
        #целевого
    elif call.data == 'key1111':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key111'))
        doc = open("C:\\tel\\1111.txt", 'rb')
        bot.edit_message_text(doc, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
        #классового
    elif call.data == 'key1112':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key111'))
        doc = open("C:\\tel\\1112.txt", 'rb')
        bot.edit_message_text(doc, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
    #совместного
        # целевого
    elif call.data == 'key1121':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key112'))
        doc = open("C:\\tel\\1121.txt", 'rb')
        bot.edit_message_text(doc, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
        # классового
    elif call.data == 'key1122':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key112'))
        doc = open("C:\\tel\\1122.txt", 'rb')
        bot.edit_message_text(doc, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
    #кастодиального
        # целевого
    elif call.data == 'key1131':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key113'))
        doc = open("C:\\tel\\1131.txt", 'rb')
        bot.edit_message_text(doc, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
        # классового
    elif call.data == 'key1132':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key113'))
        doc = open("C:\\tel\\1132.txt", 'rb')
        bot.edit_message_text(doc, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
    #присоединенного
        #нового
    elif call.data == 'key121':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key12'))
        doc = open("C:\\tel\\121.txt", 'rb')
        bot.edit_message_text(doc, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
        #присоединение уже открытого
    elif call.data == 'key122':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key12'))
        doc = open("C:\\tel\\122.txt", 'rb')
        bot.edit_message_text(doc, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
    #Ветка пополнения
    #интегрального
        #взиморасчет
    elif call.data == 'key211':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key21'))
        doc = open("C:\\tel\\211.txt", 'rb')
        bot.edit_message_text(doc, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
        #SWIFT - Maxpe LTD - City
    elif call.data == 'key212':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key21'))
        doc = open("C:\\tel\\212.txt", 'rb')
        bot.edit_message_text(doc, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
        #SWIFT - City
    elif call.data == 'key213':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key21'))
        doc = open("C:\\tel\\213.txt", 'rb')
        bot.edit_message_text(doc, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
    #присоединенного
        #Тинькофф (Юани)
    elif call.data == 'key221':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key22'))
        doc = open("C:\\tel\\221.txt", 'rb')
        bot.edit_message_text(doc, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
        #Доллары SWIFT
    elif call.data == 'key222':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key22'))
        doc = open("C:\\tel\\222.txt", 'rb')
        bot.edit_message_text(doc, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
    #ветка вывода и закрытия
        #Вывод с IB (всегда сначала)
    elif call.data == 'key31':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key3'))
        doc = open("C:\\tel\\31.txt", 'rb')
        bot.edit_message_text(doc, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
        #Вывод с интегрального (разово, часть, закрытие)
    elif call.data == 'key32':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key3'))
        doc = open("C:\\tel\\32.txt", 'rb')
        bot.edit_message_text(doc, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
    #Ветка команда
    elif call.data == 'key41':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key0'))
        doc = open("C:\\tel\\41.txt", 'rb')
        bot.edit_message_text(doc, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)


bot.polling()
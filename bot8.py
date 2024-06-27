#бот с инлайн кнопками
import telebot
#модуль для работы с ReplyKeyboardMarkup кнопками
from telebot import types
import Config
from gdisk1 import *
bot = telebot.TeleBot(Config.TOKEN)
#Инициализация бота
@bot.message_handler(commands=['start'])
#стартовое меню
def start_message(message):
    keyboard_category = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_category.add(types.KeyboardButton(text='работа со счетом'))
    bot.send_message(message.chat.id, text="Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, "
                                           "бот созданный чтобы быть финансовым консультантом. Для начала выберите категорию услуги.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=keyboard_category)
#Обработка меню
@bot.message_handler(content_types=["text"])
#основное меню
def next_message(message):
    if message.text.lower() == 'работа со счетом':
        keyboard_subcategory = types.InlineKeyboardMarkup(row_width=1)
        button1 = types.InlineKeyboardButton('Открытие', callback_data='key1')
        button2 = types.InlineKeyboardButton('Пополнение', callback_data='key2')
        button3 = types.InlineKeyboardButton('Вывод', callback_data='key3')
        button4 = types.InlineKeyboardButton('Закрытие', callback_data='key4')
        button5 = types.InlineKeyboardButton('Команда', callback_data='key5')
        keyboard_subcategory.add(button1, button2, button3, button4, button5)
        bot.send_message(message.chat.id, text='Выберите операцию', reply_markup=keyboard_subcategory)
    else:
        bot.send_message(message.chat.id, text='Недоступная операция')
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'key0':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Открытие', callback_data='key1'),
                           types.InlineKeyboardButton('Пополнение', callback_data='key2'),
                           types.InlineKeyboardButton('Вывод', callback_data='key3'),
                           types.InlineKeyboardButton('Закрытие', callback_data='key4'),
                           types.InlineKeyboardButton('Команда', callback_data='key5'))
        bot.edit_message_text('Выберите операцию', call.message.chat.id, call.message.message_id,
                              reply_markup=keyboard_tovar)
#ветка открытие1
    elif call.data == 'key1':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Интегральный', callback_data='key11'),
                           types.InlineKeyboardButton('Присоединенный (Прямой брокерский)', callback_data='key12'),
                           types.InlineKeyboardButton('Назад', callback_data='key0'))
        answer = read_file(id_file='16BN8K17VBl039QvQQJA5o9mw3edzqjLs')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
    #Интегральный11
    elif call.data == 'key11':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Именной', callback_data='key111'),
                           types.InlineKeyboardButton('Совместный', callback_data='key112'),
                           types.InlineKeyboardButton('Кастодиальный', callback_data='key113'),
                           types.InlineKeyboardButton('Назад', callback_data='key1'))
        answer = read_file(id_file='1hQGGwzuGyyy-O8YrhFZuddjueDCEjxjr')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
        #Именной111
    elif call.data == 'key111':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Целевой (от 2283$)', callback_data='key1111'),
                           types.InlineKeyboardButton('Классовый/VIP (от 50 000$', callback_data='key1112'),
                           types.InlineKeyboardButton('Назад', callback_data='key11'))
        answer = read_file(id_file='1I-736VEJkggqDcSgUwd8IiTxPhHflJBF')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
        #Целевой1111
    elif call.data == 'key1111':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('В программе SunRise', callback_data='key11111'),
                           types.InlineKeyboardButton('В PDF редакторе', callback_data='key11112'),
                           types.InlineKeyboardButton('Назад', callback_data='key111'))
        answer = read_file(id_file='1Gtdn1At9rp7D9ttBPcP8EpQiq6YwbWxt')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
        # Классовый1112
    elif call.data == 'key1112':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('В программе SunRise', callback_data='key11121'),
                           types.InlineKeyboardButton('В PDF редакторе', callback_data='key11122'),
                           types.InlineKeyboardButton('Назад', callback_data='key111'))
        answer = read_file(id_file='1Zve8sPNcIlHf-m9UvlK8mgfb1z1A30Xi')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
        #Совместный112
    elif call.data == 'key112':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Целевой (от 2283$)', callback_data='key1121'),
                           types.InlineKeyboardButton('Классовый/VIP (от 50 000$', callback_data='key1122'),
                           types.InlineKeyboardButton('Назад', callback_data='key11'))
        answer = read_file(id_file='1QpzUKuq2wQtn1co6ary2DBlHmLK5bwfC')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
        #Кастодиальный113
    elif call.data == 'key113':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Целевой (от 2283$)', callback_data='key1131'),
                           types.InlineKeyboardButton('Классовый/VIP (от 50 000$', callback_data='key1132'),
                           types.InlineKeyboardButton('Назад', callback_data='key11'))
        answer = read_file(id_file='1cL_4JNCtgZEs4RXTrLngUjVt93Zx2nYz')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
    #Присоединенный12
    elif call.data == 'key12':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Новый', callback_data='key121'),
                           types.InlineKeyboardButton('Присоединение уже открытого', callback_data='key122'),
                           types.InlineKeyboardButton('Назад', callback_data='key1'))
        answer = read_file(id_file='1qxo7SF2MxWweagUEl_OVCk0QGQKxG2t9')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
#ветка пополнение2
    elif call.data == 'key2':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Интегральный', callback_data='key21'),
                           types.InlineKeyboardButton('Присоединенный (Прямой брокерский)', callback_data='key22'),
                           types.InlineKeyboardButton('Назад', callback_data='key0'))
        answer = read_file(id_file='1e4YQ-TvJ5Mcah6LhGQy4WotL_eyTj3dE')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
    #интегральный21
    elif call.data == 'key21':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Взаиморасчет', callback_data='key211'),
                           types.InlineKeyboardButton('SWIFT - Maxpe LTD - City', callback_data='key212'),
                           types.InlineKeyboardButton('SWIFT - City', callback_data='key213'),
                           types.InlineKeyboardButton('Назад', callback_data='key2'))
        answer = read_file(id_file='1eODbsS-9vhip-SZNkXoeFKt_ayvFhSZq')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)

        #SWIFT - Maxpe LTD - City212
    elif call.data == 'key212':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Доллар', callback_data='key2121'),
                           types.InlineKeyboardButton('Евро', callback_data='key2122'),
                           types.InlineKeyboardButton('Рубли', callback_data='key2123'),
                           types.InlineKeyboardButton('Лиры', callback_data='key2124'),
                           types.InlineKeyboardButton('Назад', callback_data='key21'))
        answer = read_file(id_file='1K4bGyi2ZJdxDjgcZMFNsgdCtmPYFRP2O')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
    #Присоединенный22
    elif call.data == 'key22':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Тинькофф (Юани)', callback_data='key221'),
                           types.InlineKeyboardButton('Доллары SWIFT', callback_data='key222'),
                           types.InlineKeyboardButton('Назад', callback_data='key2'))
        answer = read_file(id_file='19iBC1mog2cnAJwz6h2Pl86ugiXlucWLd')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
#ветка вывод и закрытие3
    #elif call.data == 'key3':
    #    keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
    #    keyboard_tovar.add(types.InlineKeyboardButton('Вывод с IB (всегда сначала)', callback_data='key31'),
    #                       types.InlineKeyboardButton('Вывод с интегрального (разово, часть, закрытие)', callback_data='key32'),
    #                       types.InlineKeyboardButton('Назад', callback_data='key0'))
    #    #bot.edit_message_text('Выберите подкатегорию закрытия и вывода денег с счета', call.message.chat.id, call.message.message_id,
    #    #                      reply_markup=keyboard_tovar)
    #    bot.edit_message_text(open("C:\\tel\\3.txt", 'rb'), call.message.chat.id, call.message.message_id,
    #                          reply_markup=keyboard_tovar)
#ветка команда5
    #elif call.data == 'key5':
    #    keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
    #    keyboard_tovar.add(types.InlineKeyboardButton('Активация личного кабинета', callback_data='key51'),
    #                       types.InlineKeyboardButton('Назад', callback_data='key0'))
    #    #bot.edit_message_text('Выберите команду', call.message.chat.id, call.message.message_id,
    #    #                      reply_markup=keyboard_tovar)
    #    bot.edit_message_text(open("C:\\tel\\5.txt", 'rb'), call.message.chat.id, call.message.message_id,
    #                          reply_markup=keyboard_tovar)
#def end_message(message):
#обработка конечных кнопок
#нужно придумать как сократить код: можно сделать общий вызов кнопки назад
#ветка открытие
    #именного
        #целевого1111
        #В программе SunRise11111
    elif call.data == 'key11111':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key1111'))
        answer = read_file(id_file='1zOlh9RKwU0rnSh3jv-3aHSrbXKCB_nrK')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
        #В PDF редакторе
    elif call.data == 'key11112':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key1111'))
        answer = read_file(id_file='1eXF5nhxclcHco149iyWeCJ27ufI2-CIS')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
        #классового1112
        # В программе SunRise11121
    elif call.data == 'key11121':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key1112'))
        answer = read_file(id_file='1oTdJ4daaIdS-YuqjCgGYVW_aAgdgqyPk')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
        # В PDF редакторе11122
    elif call.data == 'key11122':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key1112'))
        answer = read_file(id_file='1z6wDJ_KvOFLldKfukHnrs23nxGzUnEii')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
    #совместного
        # целевого
    elif call.data == 'key1121':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key112'))
        answer = read_file(id_file='1GIauXWSBS2_CrAsDHqDaJ8ywhmmUKts4')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
        # классового
    elif call.data == 'key1122':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key112'))
        answer = read_file(id_file='1iXYJl7R-UM0zloHTRM6V7woneaV4HUr_')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
    #кастодиального
        # целевого
    elif call.data == 'key1131':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key113'))
        answer = read_file(id_file='1ITXeWGAhysnqF7qzIK89M8J0-Ud7ynsh')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
        # классового
    elif call.data == 'key1132':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key113'))
        answer = read_file(id_file='1jycJkgaXaA8ov4KhnonmyLXf6MVXOkee')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
    #присоединенного
        #нового
    elif call.data == 'key121':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key12'))
        answer = read_file(id_file='18pGyAC-LxJ4sTw_xyiTW79aMCEDM5GUM')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
        #присоединение уже открытого
    elif call.data == 'key122':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key12'))
        answer = read_file(id_file='1cE7WRnyaqaZ9ilC8ThRoEcVILtWrC8eZ')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
    #Ветка пополнения
    #интегрального
        #взиморасчет
    elif call.data == 'key211':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key21'))
        answer = read_file(id_file='12vl90zl3Wq3OGCR36l5Va8XFeiYs4F2m')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
        #SWIFT - Maxpe LTD - City
        #Доллар
    elif call.data == 'key2121':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key212'))
        answer = read_file(id_file='1LDnfx0LahbjM6zAyUDNyRKm1cARPgkGI')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
        #Евро
    elif call.data == 'key2122':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key212'))
        answer = read_file(id_file='18uvOD5FnorGHXD-xzIeDke4CPWmnI_kc')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
        #Рубли
    elif call.data == 'key2123':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key212'))
        answer = read_file(id_file='1OcFQ2GMhgOPaDmPoBbLKxz1n74NagynI')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
        #Лиры
    elif call.data == 'key2124':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key212'))
        answer = read_file(id_file='15S0EiidmkEU30B1EzTLEizwaH7fvHayC')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
        #SWIFT - City
    elif call.data == 'key213':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key21'))
        answer = read_file(id_file='19CxFT-oloyZ9u2iglca3YaU9uhrjPzBJ')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
    #присоединенного
        #Тинькофф (Юани)
    elif call.data == 'key221':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key22'))
        answer = read_file(id_file='1EBPOJb0cbRHq8Wf-oHlEcEdILEVf-V0P')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
        #Доллары SWIFT
    elif call.data == 'key222':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key22'))
        answer = read_file(id_file='1L7EKkQSG7L6o00ZTfPQ2t_oLNsQIjOOB')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)
    #ветка вывода и закрытия
    #вывод
    elif call.data == 'key3':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key0'))
        answer = read_file(id_file='1vx-VU79gnQIVfb1ZEa7oAXEuODZQUIOU')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id,
                              reply_markup=keyboard_tovar)
    #закрытие
    elif call.data == 'key4':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key0'))
        answer = read_file(id_file='1HPyjS65Zs59cplr2kVkuaxNXjzCrKlBK')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)

        # Вывод с IB (всегда сначала)
    #elif call.data == 'key31':
    #    keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
    #    keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key3'))
    #    bot.edit_message_text(open("C:\\tel\\31.txt", 'rb'), call.message.chat.id, call.message.message_id,
    #                          reply_markup=keyboard_tovar)
    #    #Вывод с интегрального (разово, часть, закрытие)
    #elif call.data == 'key32':
    #    keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
    #    keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key3'))
    #    bot.edit_message_text(open("C:\\tel\\32.txt", 'rb'), call.message.chat.id, call.message.message_id,
    #                          reply_markup=keyboard_tovar)
    #Ветка команда5
    elif call.data == 'key5':
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=1)
        keyboard_tovar.add(types.InlineKeyboardButton('Назад', callback_data='key0'))
        answer = read_file(id_file='15ZTmakZ2OQaht6ztr6VDY_tvwFoiweoZ')
        bot.edit_message_text(answer, call.message.chat.id, call.message.message_id, reply_markup=keyboard_tovar)


bot.polling()
import telebot
from extens import Apiexeption, Rateconverter
from config import keys, TOKEN

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате:\n<Имя валюты, цену которой хочешь узнать> ' \
    '<Имя валюты, в которой нужно узнать цену первой валюты> ' \
    '<Колличество переводимой валюты>\n Увидить список всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')
    try:
        if len(values) != 3:
            raise Apiexeption('Неверное количество параметров!')

        answer = Rateconverter.get_price(*values)
    except Apiexeption as e:
        bot.reply_to(message, f"Ошибка в команде:\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Неизвестная ошибка:\n{e}")
    else:
        bot.reply_to(message, answer)

bot.polling()

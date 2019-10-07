import telebot
from telebot import types
import sqlite3

start_text = 'Генерировать вопрос'
TOKEN = '917337579:AAEUzL3MkAWwlrD4xorDAu7H65j0wHFYWOY'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_action(message):
    start_menu = types.ReplyKeyboardMarkup(True, False)
    start_menu.row(start_text)

    bot.send_message(message.chat.id, 'Хэй! Я бот для игры в "Я никогда не" :)\nНажми на кнопку и я придумаю тебе ситуацию', reply_markup=start_menu)
	
@bot.message_handler(content_types=['text'])
def main_action(message):
    if message.text == start_text:
        conn = sqlite3.connect("questions.db")
        cursor = conn.cursor()
        question = cursor.execute("SELECT question FROM questions ORDER BY RANDOM() LIMIT 1")
	
        bot.send_message(message.chat.id, 'Я никогда не ' + cursor.fetchone()[0])
		
bot.polling();
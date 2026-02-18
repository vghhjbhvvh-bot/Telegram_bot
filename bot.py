import random
import telebot
from telebot import types

bot = telebot.TeleBot('YOUR_BOT_TOKEN')

challenges = [
    'Write a short story about a character who discovers a hidden world.',
    'Create a new language and write a short conversation between two people.',
    'Design a new species of animal and describe its habitat and behavior.',
    'Write a poem about a memory from your childhood.',
    'Create a new game and explain its rules and objectives.'
]

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Welcome to the Random Challenge Bot!')
    bot.send_message(message.chat.id, 'Type /challenge to receive a random challenge.')

@bot.message_handler(commands=['challenge'])
def challenge(message):
    challenge = random.choice(challenges)
    bot.send_message(message.chat.id, challenge)

bot.polling()
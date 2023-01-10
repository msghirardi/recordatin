from config import *
import telebot
import requests
import json


# instanciamos el bot de Telegram
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# responde al comando /start
@bot.message_handler(commands=["start", "ayuda", "help"])
def cmd_start(message):
    # Da la bienvenida al usuario
    bot.reply_to(message, "Bienvenida! Este es mi primer bot")


@bot.message_handler(commands=["horario"])
def cmd_start(message):
    bot.reply_to(message, "Se recomienda antes de las 8am, o bien, pasadas las 19pm")


# Responde al mensaje que no son comandos
@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    # Gestiona los mensajes de texto recibidos
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "Comando no disponible")
    else:
        bot.send_message(
            message.chat.id, "Todavia no entiendo lo que me estas diciendo"
        )


if __name__ == "__main__":
    print("Iniciando bot")
    bot.infinity_polling()
    print("Fin")

import telepot
import sys

token = 'здесь токен'
chat_id = 12345678

TelegramBot = telepot.Bot(token)


def send_message_to_telegrambot(message):
    TelegramBot.sendMessage(chat_id, message)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        send_message_to_telegrambot(sys.argv[1])
    else:
        send_message_to_telegrambot('no message')

import telepot
import sys
import _falkov_params as _fp


def send_message_to_telegrambot(message):
    telegram_bot = telepot.Bot(_fp.tel_token)
    telegram_bot.sendMessage(_fp.tel_chat_id, message)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        send_message_to_telegrambot(sys.argv[1])
    else:
        send_message_to_telegrambot('no message')

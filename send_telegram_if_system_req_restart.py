import os
import send_to_telegrambot

reboot_required_filename = '/var/run/reboot-required'

if __name__ == "__main__":
    if os.path.exists(reboot_required_filename):
        send_to_telegrambot.send_message_to_telegrambot('*** DO: System restart required ***')

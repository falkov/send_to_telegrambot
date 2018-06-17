import requests
import telepot
import subprocess

import _falkov_params as _fp


def ip_information(ip_str):
    url = f'http://api.sypexgeo.net/json/{ip_str}'
    ip_inform = ''

    try:
        process = subprocess.Popen(["nslookup", ip_str], stdout=subprocess.PIPE)
        output = str(process.communicate()[0])
    except Exception as err:
        output = ''
        print(err)

    home_index = output.find('name')

    if home_index > 0:
        end_index = output.find('\\n', home_index)
        hostname = output[home_index+7:end_index-1]
    else:
        hostname = None

    try:
        r_json = requests.get(url).json()
    except requests.RequestException:
        ip_inform = f"{ip_str} - exception - {url}"
    else:
        ip = r_json.get('ip')

        city = r_json.get('city')
        if city: city = r_json.get('city').get("name_en")

        country = r_json.get('country')
        if country: country = r_json.get('country').get("name_en")

        ip_inform = f"{ip} - {city} - {country} - {hostname}"
    finally:
        return ip_inform


def send2telegram_ipinformation(prefix_str, ip_str):
    token = _fp.tel_token
    telegram_bot = telepot.Bot(token)
    chat_id = _fp.tel_chat_id

    message = ip_information(ip_str)
    telegram_bot.sendMessage(chat_id, message)

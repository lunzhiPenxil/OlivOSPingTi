import OlivOS
import OlivOSPingTi

import json
import requests as req

class Event(object):
    def init(plugin_event, Proc):
        pass

    def init_after(plugin_event, Proc):
        pass

    def private_message(plugin_event, Proc):
        pass

    def private_message_sent(plugin_event, Proc):
        pass

    def group_message(plugin_event, Proc):
        unity_reply(plugin_event, Proc)

    def poke(plugin_event, Proc):
        pass

    def save(plugin_event, Proc):
        pass

    def menu(plugin_event, Proc):
        pass

def unity_reply(plugin_event:OlivOS.API.Event, Proc:OlivOS.pluginAPI.shallow):
    msg = plugin_event.data.message.lower()
    if type(msg) is str \
    and (msg.startswith('/pingti') \
    or msg.startswith('/pt') \
    or msg.startswith('/平替') \
    or msg.startswith('.pingti') \
    or msg.startswith('.pt') \
    or msg.startswith('.平替')):
        if msg.startswith('/pingti'):
            msg = msg.lstrip('/pingti')
        elif msg.startswith('/pt'):
            msg = msg.lstrip('/pt')
        elif msg.startswith('/平替'):
            msg = msg.lstrip('/平替')
        elif msg.startswith('.pingti'):
            msg = msg.lstrip('.pingti')
        elif msg.startswith('.pt'):
            msg = msg.lstrip('.pt')
        elif msg.startswith('.平替'):
            msg = msg.lstrip('.平替')
        msg = msg.strip(' ')
        send_text = getAnswer(msg)
        if send_text is not None:
            send_text = send_text.encode('latin1').decode('utf-8')
            plugin_event.reply(f'[{msg}]的平替是:\n{send_text}')
        else:
            plugin_event.reply('找不到喵')

def poke_reply(plugin_event, Proc):
    pass

def getAnswer(itemName:str):
    res = None
    tmp_res = None
    tmp_value = json.dumps(
        {
            "messages": [
                {
                    "role": "user",
                    "content": f"{itemName}"
                }
            ]
        }
    )
    send_url = 'https://www.pingti.xyz/api/chat'
    headers = {
        'User-Agent': 'OlivOS/1.0.0'
    }
    try:
        msg_res = req.request("POST", send_url, headers = headers, data = tmp_value)
        tmp_res = str(msg_res.text)
        res = tmp_res
    except:
        pass
    return res


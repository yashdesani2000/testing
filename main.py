from gujarat_samachar import *
from sandesh import *
import requests

s = requests.Session()


gs_today = ['2022-07-21']
sandesh_today = ['2022-07-21'] 

while True:
    s.get('https://api.telegram.org/bot5501050196:AAGL4UdZEPszxSMPwgnBdXoViykBA8vy3c4/sendmessage?chat_id=1124985872&text=hii')
    if gs_today[0] == gs_date():
        gs_today.clear()
        n = open('stickers\\gujarat_samachar.webp', 'rb')
        file = {'sticker': n}
        s.post('https://api.telegram.org/bot5501050196:AAGL4UdZEPszxSMPwgnBdXoViykBA8vy3c4/sendSticker?chat_id=1124985872', files=file)
        n.close()
        gs_main_edition()
        gs_district_edition()
        gs_magazines()
        gs_today.append(date.today()+timedelta(1))
    else:
        pass
    if sandesh_today[0] == sandesh_date():
        sandesh_today.clear()
        n = open('stickers\\sandesh.webp', 'rb')
        file = {'sticker': n}
        s.post('https://api.telegram.org/bot5501050196:AAGL4UdZEPszxSMPwgnBdXoViykBA8vy3c4/sendSticker?chat_id=1124985872', files=file)
        n.close()
        sandesh_url()
        sandesh_main_edition()
        sandesh_magazines_url()
        sandesh_magazines()
        sandesh_today.append(date.today()+timedelta(1))
    else:
        pass

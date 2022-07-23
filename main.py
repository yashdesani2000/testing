from gujarat_samachar import *
from sandesh import *
from datetime import *
import requests, time


s = requests.Session()


gs_today = ['2022-07-22']
sandesh_today = ['2022-07-22'] 

while True:
    gs = gs_date()
    sandesh = sandesh_date()
    # print(gs, sandesh, gs_today[0], sandesh_today[0])
    s.get('https://api.telegram.org/bot5501050196:AAGL4UdZEPszxSMPwgnBdXoViykBA8vy3c4/sendmessage?chat_id=1124985872&text='+str(gs)+' , '+str(sandesh)+' , '+str(gs_today[0])+' , '+str(sandesh_today[0]))
    if str(gs_today[0]) == str(gs):
        gs_today.clear()
        n = open('gujarat_samachar.webp', 'rb')
        file = {'sticker': n}
        s.post('https://api.telegram.org/bot5501050196:AAGL4UdZEPszxSMPwgnBdXoViykBA8vy3c4/sendSticker?chat_id=1124985872', files=file)
        n.close()
        gs_main_edition()
        gs_district_edition()
        gs_magazines()
        gs_today.append(date.today()+timedelta(1))
    else:
        pass
    if str(sandesh_today[0]) == str(sandesh):
        sandesh_today.clear()
        n = open('sandesh.webp', 'rb')
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
    time.sleep(60)
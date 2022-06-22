import requests
from bs4 import BeautifulSoup
import random

s = requests.Session()

proxies = open('yash.txt').read().splitlines()
ua = open('user_agents.txt').read().splitlines()

url = 'https://techdesani.blogspot.com/2022/06/hi-yash.html'


for ip in proxies:
    rdm = random.choice(ua)
    # print(rdm)
    header = { 
    'user-agent': rdm}
    list = ['socks4://'+ip, 'socks5://'+ip]
    for i in list:
        try:
            res = s.get(url, headers=header, proxies={'https': i, 'http': i})
            # print(res.text)
            soup = BeautifulSoup(res.text, 'lxml')
            # print(soup)
            hi = soup.find('div', class_='post-body entry-content')
            # print(ip, 'working')
        except:
            print("n")
open('yash.txt').close()
open('user_agents.txt').close()
api = "https://api.telegram.org/bot5317123296:AAE7U6qJdnkhL19_AZfKiDWuq-752j0VGe8/sendmessage?chat_id=-1001677829704&text=Finished"
#b = requests.get(api)

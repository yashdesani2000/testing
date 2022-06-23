import requests
import random
from list import user_agents

# f = open('user_agent.txt').read().splitlines()

proxy = []
# r = random.choice(user_agents)
# print(r)

def socks5():   
        url = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5'
        s = requests.Session()
        res = s.get(url).text.splitlines()
        for i in res:
                proxy.append(i)  
        for p in range(10):
                print(len(proxy))
                user_agent = random.choice(user_agents)
                url2 = 'https://www.yashdesani.tk/2022/06/hi-yash.html'
                header = { 'user-agent': user_agent}
                s = requests.Session()
                ip = random.choice(proxy)
                list = ['socks4://'+ip, 'socks5://'+ip]
                if user_agent != None:
                        print(user_agent)
                        for i in list:
                                try:
                                        s.get(url=url2, headers=header, proxies={'https': i, 'http': i}, timeout=5)
                                        print(p, i, 'working')
                                except:
                                        print(p, i, 'dead')
                                       

while True:
        requests.get('https://api.telegram.org/bot5317123296:AAE7U6qJdnkhL19_AZfKiDWuq-752j0VGe8/sendmessage?chat_id=-1001677829704&text=hiii')
        proxy.clear()
        print('refreshed')
        socks5()
 


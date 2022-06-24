import requests
import random
from list import user_agents

# f = open('user_agent.txt').read().splitlines()
print("Running")
proxy = []
# r = random.choice(user_agents)
# print(r)

def socks5():   
        url = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5'
        s = requests.Session()
        res = s.get(url).text.splitlines()
        for i in res:
                proxy.append(i)  
        for p in range(30):
                user_agent = random.choice(user_agents)
                url2 = 'https://www.yashdesani.tk/2022/06/hi-yash.html'
                header = { 'user-agent': user_agent}
                s = requests.Session()
                ip = random.choice(proxy)
            
                if user_agent != None:
                        try:
                            s.get(url=url2, headers=header, proxies={'https': 'socks5://'+ip, 'http': 'socks5://'+ip}, timeout=5)
                            print(p, i, 'working')
                        except:
                                        pass
                                       

while True:
        requests.get('https://api.telegram.org/bot5501050196:AAHggL5bXIlyRtCGukPY70huqD-k_OKgc-0/sendmessage?chat_id=1124985872&text=refreshed')
        proxy.clear()
        socks5()
 


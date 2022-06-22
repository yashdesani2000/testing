import requests, time

url = "https://api.telegram.org/bot5317123296:AAE7U6qJdnkhL19_AZfKiDWuq-752j0VGe8/sendmessage?chat_id=-1001677829704&text="

f = open('yash.txt').read().splitlines()

s = requests.Session()

for i in f:
    time.sleep(2)
    res = s.get(url+i)
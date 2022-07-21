import requests, datetime, os
from io import BytesIO
import img2pdf

today = datetime.date.today()

editions = ['ahmedabad','ahmedabad-east','city-life','zalawad---ahmedabad-dist','gandhinagar','kheda','mehsana','sabarkantha','patan','surat','surat-dist','valsad','navsari','rajkot','halar','junagadh','saurashtra','vadodara','vadodara-dist','panchmahal---dahod','bharuch','bhuj','bhavnagar']

url_list = []

magazines_editions = ['business-sandesh','savdhan-no-tabacco-day','nari','ardha-saptahik','shradha','nakshatra','cine-sandesh','kids','sanskar','varshik-rashifal']

magazines_url_list = []

s = requests.Session()

def sandesh_date():
    res = s.get('https://wapi.sandesh.com/api/v1/tithi').json()
    sandesh_date = res['data']['date']
    return sandesh_date

def sandesh_url():
    try:
        for i in editions:
            url = 'https://wapi.sandesh.com/api/v1/e-paper?slug='+i+'&date='+str(today)
            url_list.append(url)
    except:
        pass

def sandesh_main_edition():
    try:
        for i in range(len(url_list)):
            res = s.get(url_list[i]).json()   
            total_pages = res['data']['sub']
            pdf_name = res['query']['slug']
            # print(len(total_pages),pdf_name)
            images = []

            for i in range(len(total_pages)):
                try:
                    img_url = total_pages[i]['photo'].split('?w')[0]
                    res = s.get("https://esandesh.gumlet.io/"+img_url)
                    images.append(BytesIO(res.content))
                except:
                    pass    

            f = open('Sandesh\\'+pdf_name+'.pdf', 'wb')
            f.write(img2pdf.convert(images))
            f.close()
            n = open('Sandesh\\'+pdf_name+'.pdf', 'rb')
            file = {'document': n}
            s.post('https://api.telegram.org/bot5501050196:AAGL4UdZEPszxSMPwgnBdXoViykBA8vy3c4/senddocument?chat_id=1124985872', files=file)
            n.close()
            os.remove('Sandesh\\'+pdf_name+'.pdf')
    except:
        pass

def sandesh_magazines_url():
    try:
        for i in magazines_editions:
            url = 'https://wapi.sandesh.com/api/v1/e-paper?slug='+i+'&date='+str(today)
            magazines_url_list.append(url)
    except:
        pass

def sandesh_magazines():
    try:
        for i in range(len(magazines_url_list)):
            res = s.get(magazines_url_list[i]).json()   
            total_pages = res['data']['sub']
            pdf_name = res['query']['slug']
            date = res['data']['main'][0]['date']
            # print(len(total_pages),pdf_name)
            images = []
   
            if str(date) == str(today):
                for i in range(len(total_pages)):
                    try:
                        img_url = total_pages[i]['photo'].split('?w')[0]
                        res = s.get("https://esandesh.gumlet.io/"+img_url)
                        images.append(BytesIO(res.content))
                    except:
                        pass    

                f = open('Sandesh\\'+pdf_name+'.pdf', 'wb')
                f.write(img2pdf.convert(images))
                f.close()
                n = open('Sandesh\\'+pdf_name+'.pdf', 'rb')
                file = {'document': n}
                s.post('https://api.telegram.org/bot5501050196:AAGL4UdZEPszxSMPwgnBdXoViykBA8vy3c4/senddocument?chat_id=1124985872', files=file)
                n.close()
                os.remove('Sandesh\\'+pdf_name+'.pdf')
            else:
                pass    
    except:
        pass
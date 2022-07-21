import requests, os
from bs4 import BeautifulSoup
from io import BytesIO
import img2pdf
from datetime import *


url = 'https://epaper.gujaratsamachar.com/'

s = requests.Session()

res = s.get(url)

soup = BeautifulSoup(res.text,'lxml')

all_news_papers = soup.find('div', id='ajax_data')

def gs_date():
    gs_dt = soup.find('script', type='text/javascript').text.split("$('span.date').text")[1].split(';')[0].strip('("")').split('-')
    gs_date = gs_dt[2]+'-'+gs_dt[1]+'-'+gs_dt[0]
    return gs_date

def gs_main_edition():
    try:
        main_editions = all_news_papers.find('div', id='tab1').find('div', class_='row').find_all('div', class_='col-sm-6 col-md-4 text-center d-flex flex-column')
        name = all_news_papers.find('div', id='tab1').find('div', class_='row').find_all('div', class_='d-flex flex-column flex-md-row align-items-center justify-content-center mt-3 mb-3 flex-wrap')
        names = []
        for i in name:
            names.append(i.h6.text)


        main_edition_links = []

        for i in main_editions:
            main_news_paper = i.find('div', class_='box p-3 d-flex justify-content-center').a['href']
            # print(main_news_paper)
            main_edition_links.append(main_news_paper)

        images = []

        for i in range(len(main_edition_links)):
            images.clear()
            pages = s.get(main_edition_links[i])
            extract_page = BeautifulSoup(pages.text,'lxml')
            total_pages = extract_page.find('div', class_='d-flex w-100 nav-dots-otr justify-content-center').ul.find_all('li')
            base_page_url = extract_page.find_all('div', class_='container-fluid')[2].find('div',class_='row align-items-lg-start').find('div',class_='col-xl-7 min-section').div.div.img['src'].split('0.')[0]
            pdf_name = names[i]
            #print(len(total_pages), pdf_name)

            for p in range(len(total_pages)):
                try:
                    url = base_page_url+str(p)+'.jpg'
                    res = s.get(url)
                    images.append(BytesIO(res.content))
                except:
                    pass

            f = open('Gujarat Samachar\\'+pdf_name+'.pdf', 'wb')
            f.write(img2pdf.convert(images))
            f.close()
            n = open('Gujarat Samachar\\'+pdf_name+'.pdf', 'rb')
            file = {'document': n}
            s.post('https://api.telegram.org/bot5501050196:AAGL4UdZEPszxSMPwgnBdXoViykBA8vy3c4/senddocument?chat_id=1124985872', files=file)
            n.close()
            os.remove('Gujarat Samachar\\'+pdf_name+'.pdf')
    except:
        pass

def gs_district_edition():
    try: 
        district_edition = all_news_papers.find('div', id='tab2').find('div', class_='row').find_all('div', class_='col-sm-6 col-md-4 text-center d-flex flex-column')
        name = all_news_papers.find('div', id='tab2').find('div', class_='row').find_all('div', class_='d-flex flex-column flex-md-row align-items-center justify-content-center mt-3 mb-3')
        names = []
        for i in name:
            names.append(i.h6.text)

        district_edition_links = []

        for i in district_edition:
            main_news_paper = i.find('div', class_='box p-3 d-flex justify-content-center').a['href']
            # print(main_news_paper)
            district_edition_links.append(main_news_paper)

        images = []

        for i in range(len(district_edition_links)):
            images.clear()
            pages = s.get(district_edition_links[i])
            extract_page = BeautifulSoup(pages.text,'lxml')
            total_pages = extract_page.find('div', class_='d-flex w-100 nav-dots-otr justify-content-center').ul.find_all('li')
            base_page_url = extract_page.find_all('div', class_='container-fluid')[2].find('div',class_='row align-items-lg-start').find('div',class_='col-xl-7 min-section').div.div.img['src'].split('0.')[0]
            pdf_name = names[i]
            #print(len(total_pages), pdf_name)

            for p in range(len(total_pages)):
                try:
                    url = base_page_url+str(p)+'.jpg'
                    res = s.get(url)
                    images.append(BytesIO(res.content))
                except:
                    pass
            
            f = open('Gujarat Samachar\\'+pdf_name+'.pdf', 'wb')
            f.write(img2pdf.convert(images))
            f.close()
            n = open('Gujarat Samachar\\'+pdf_name+'.pdf', 'rb')
            file = {'document': n}
            s.post('https://api.telegram.org/bot5501050196:AAGL4UdZEPszxSMPwgnBdXoViykBA8vy3c4/senddocument?chat_id=1124985872', files=file)
            n.close()
            os.remove('Gujarat Samachar\\'+pdf_name+'.pdf')
    except:
        pass

def gs_magazines():
    try:
        day = datetime.today().weekday()
        magazines = all_news_papers.find('div', id='tab3').find('div', class_='row').find_all('div', class_='col-sm-6 col-md-4 text-center d-flex flex-column')
        name = all_news_papers.find('div', id='tab3').find_all('div', class_='d-flex flex-column flex-md-row align-items-center justify-content-center mt-3 mb-3')
        names = []
        for i in name:
            names.append(i.h6.text)


        magazines_links = []

        for i in magazines:
            main_news_paper = i.find('div', class_='box p-3 h-100 d-flex justify-content-center').a['href']
            # print(main_news_paper)
            magazines_links.append(main_news_paper)

        images = []

        if  day == 6:
            images.clear()
            pages = s.get(magazines_links[0])
            extract_page = BeautifulSoup(pages.text,'lxml')
            total_pages = extract_page.find('div', class_='d-flex w-100 nav-dots-otr justify-content-center').ul.find_all('li')
            base_page_url = extract_page.find_all('div', class_='container-fluid')[2].find('div',class_='row align-items-lg-start').find('div',class_='col-xl-7 min-section').div.div.img['src'].split('0.')[0]
            pdf_name = names[0]
            #print(len(total_pages), pdf_name)

            for p in range(len(total_pages)):
                try:
                    url = base_page_url+str(p)+'.jpg'
                    res = s.get(url)
                    images.append(BytesIO(res.content))
                except:
                    pass
            f = open('Gujarat Samachar\\'+pdf_name+'.pdf', 'wb')
            f.write(img2pdf.convert(images))
            f.close()
            n = open('Gujarat Samachar\\'+pdf_name+'.pdf', 'rb')
            file = {'document': n}
            s.post('https://api.telegram.org/bot5501050196:AAGL4UdZEPszxSMPwgnBdXoViykBA8vy3c4/senddocument?chat_id=1124985872', files=file)
            n.close()
            os.remove('Gujarat Samachar\\'+pdf_name+'.pdf')

        elif day == 1:
            images.clear()
            pages = s.get(magazines_links[1])
            extract_page = BeautifulSoup(pages.text,'lxml')
            total_pages = extract_page.find('div', class_='d-flex w-100 nav-dots-otr justify-content-center').ul.find_all('li')
            base_page_url = extract_page.find_all('div', class_='container-fluid')[2].find('div',class_='row align-items-lg-start').find('div',class_='col-xl-7 min-section').div.div.img['src'].split('0.')[0]
            pdf_name = names[1]
            #print(len(total_pages), pdf_name)

            for p in range(len(total_pages)):
                try:
                    url = base_page_url+str(p)+'.jpg'
                    res = s.get(url)
                    images.append(BytesIO(res.content))
                except:
                    pass
            f = open('Gujarat Samachar\\'+pdf_name+'.pdf', 'wb')
            f.write(img2pdf.convert(images))
            f.close()
            n = open('Gujarat Samachar\\'+pdf_name+'.pdf', 'rb')
            file = {'document': n}
            s.post('https://api.telegram.org/bot5501050196:AAGL4UdZEPszxSMPwgnBdXoViykBA8vy3c4/senddocument?chat_id=1124985872', files=file)
            n.close()
            os.remove('Gujarat Samachar\\'+pdf_name+'.pdf')

        elif day == 2:
            images.clear()
            pages = s.get(magazines_links[2])
            extract_page = BeautifulSoup(pages.text,'lxml')
            total_pages = extract_page.find('div', class_='d-flex w-100 nav-dots-otr justify-content-center').ul.find_all('li')
            base_page_url = extract_page.find_all('div', class_='container-fluid')[2].find('div',class_='row align-items-lg-start').find('div',class_='col-xl-7 min-section').div.div.img['src'].split('0.')[0]
            pdf_name = names[2]
            #print(len(total_pages), pdf_name)

            for p in range(len(total_pages)):
                try:
                    url = base_page_url+str(p)+'.jpg'
                    res = s.get(url)
                    images.append(BytesIO(res.content))
                except:
                    pass
            f = open('Gujarat Samachar\\'+pdf_name+'.pdf', 'wb')
            f.write(img2pdf.convert(images))
            f.close()
            n = open('Gujarat Samachar\\'+pdf_name+'.pdf', 'rb')
            file = {'document': n}
            s.post('https://api.telegram.org/bot5501050196:AAGL4UdZEPszxSMPwgnBdXoViykBA8vy3c4/senddocument?chat_id=1124985872', files=file)
            n.close()
            os.remove('Gujarat Samachar\\'+pdf_name+'.pdf')

        elif day == 3:
            images.clear()
            pages = s.get(magazines_links[3])
            extract_page = BeautifulSoup(pages.text,'lxml')
            total_pages = extract_page.find('div', class_='d-flex w-100 nav-dots-otr justify-content-center').ul.find_all('li')
            base_page_url = extract_page.find_all('div', class_='container-fluid')[2].find('div',class_='row align-items-lg-start').find('div',class_='col-xl-7 min-section').div.div.img['src'].split('0.')[0]
            pdf_name = names[3]
            #print(len(total_pages), pdf_name)

            for p in range(len(total_pages)):
                try:
                    url = base_page_url+str(p)+'.jpg'
                    res = s.get(url)
                    images.append(BytesIO(res.content))
                except:
                    pass
            f = open('Gujarat Samachar\\'+pdf_name+'.pdf', 'wb')
            f.write(img2pdf.convert(images))
            f.close()
            n = open('Gujarat Samachar\\'+pdf_name+'.pdf', 'rb')
            file = {'document': n}
            s.post('https://api.telegram.org/bot5501050196:AAGL4UdZEPszxSMPwgnBdXoViykBA8vy3c4/senddocument?chat_id=1124985872', files=file)
            n.close()
            os.remove('Gujarat Samachar\\'+pdf_name+'.pdf')

        elif day == 4:
            images.clear()
            pages = s.get(magazines_links[4])
            extract_page = BeautifulSoup(pages.text,'lxml')
            total_pages = extract_page.find('div', class_='d-flex w-100 nav-dots-otr justify-content-center').ul.find_all('li')
            base_page_url = extract_page.find_all('div', class_='container-fluid')[2].find('div',class_='row align-items-lg-start').find('div',class_='col-xl-7 min-section').div.div.img['src'].split('0.')[0]
            pdf_name = names[4]
            #print(len(total_pages), pdf_name)

            for p in range(len(total_pages)):
                try:
                    url = base_page_url+str(p)+'.jpg'
                    res = s.get(url)
                    images.append(BytesIO(res.content))
                except:
                    pass
            f = open('Gujarat Samachar\\'+pdf_name+'.pdf', 'wb')
            f.write(img2pdf.convert(images))
            f.close()
            n = open('Gujarat Samachar\\'+pdf_name+'.pdf', 'rb')
            file = {'document': n}
            s.post('https://api.telegram.org/bot5501050196:AAGL4UdZEPszxSMPwgnBdXoViykBA8vy3c4/senddocument?chat_id=1124985872', files=file)
            n.close()
            os.remove('Gujarat Samachar\\'+pdf_name+'.pdf')

        elif day == 5:
            images.clear()
            pages = s.get(magazines_links[5])
            extract_page = BeautifulSoup(pages.text,'lxml')
            total_pages = extract_page.find('div', class_='d-flex w-100 nav-dots-otr justify-content-center').ul.find_all('li')
            base_page_url = extract_page.find_all('div', class_='container-fluid')[2].find('div',class_='row align-items-lg-start').find('div',class_='col-xl-7 min-section').div.div.img['src'].split('0.')[0]
            pdf_name = names[5]
            #print(len(total_pages), pdf_name)

            for p in range(len(total_pages)):
                try:
                    url = base_page_url+str(p)+'.jpg'
                    res = s.get(url)
                    images.append(BytesIO(res.content))
                except:
                    pass
            f = open('Gujarat Samachar\\'+pdf_name+'.pdf', 'wb')
            f.write(img2pdf.convert(images))
            f.close()
            n = open('Gujarat Samachar\\'+pdf_name+'.pdf', 'rb')
            file = {'document': n}
            s.post('https://api.telegram.org/bot5501050196:AAGL4UdZEPszxSMPwgnBdXoViykBA8vy3c4/senddocument?chat_id=1124985872', files=file)
            n.close()
            os.remove('Gujarat Samachar\\'+pdf_name+'.pdf')
    except:
        pass


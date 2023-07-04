import requests
from bs4 import BeautifulSoup
u ="https://sauda24.kz/catalog/detskie-tovary"
r = requests.get(u)
soap = BeautifulSoup(r.text,'lxml')

s =  soap.find('div',class_='fn_transfer clearfix').find('a',class_='d-flex align-items-center justify-content-center').get('aria-label')
print(s)
s2 ='https://sauda24.kz'+ soap.find('div',class_='fn_transfer clearfix').find('a',class_='product_preview__name product_preview__name_link').get('href')
listes = soap.findAll('div', class_='fn_transfer clearfix')
listes1 = len(soap.findAll('div', class_='fn_transfer clearfix'))
for lis in listes:
    data = []
    q2 = lis.find('a',class_='d-flex align-items-center justify-content-center').get('aria-label')
    if q2 != True:
        pass
    q = 'https://sauda24.kz' + lis.find('a', class_='product_preview__name product_preview__name_link').get('href')
    data.append([q2,q])
    data2 = data.copy()
    aa = open('datos.txt', 'w+', encoding='cp1251')
    aa.write(f'{data2}')
    aa = open('datos.txt', 'w+', encoding='cp1251')
    aa.read()
    print(data2)
print(len(data))
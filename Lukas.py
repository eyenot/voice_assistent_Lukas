# Creat Kazanjan Evgeny
# My github:  


from tkinter import *  
from PIL import ImageTk, Image
import speech_recognition as sr
import os
import sys
import webbrowser as web
import requests
from bs4 import BeautifulSoup
from gtts import gTTS
#-------------------------------------------------------------------------------------------------------------------------
def speak(what):
	tts = gTTS(text=what, lang='ru') 
	tts.save("pcvoice.mp3") 
	os.system("start pcvoice.mp3") 
#--------------------------------------------------------------------------------------------------------------------------
def record():
	lbl.configure(text="скажите чтонибудь")
	r = sr.Recognizer()
	with sr.Microphone(device_index = 1) as source:
		lbl.configure(text="скажите чтонибудь")
		#print("скажите чтонибудь...")
		#r.pause_threshold = 1
	#r.adjust_for_ambient_noise(source, duration=1)
		audio = r.listen(source)
	try:
		task = r.recognize_google(audio, language = "ru-RU").lower()
		print("вы сказали: "+task)
	except sr.UnknownValueError:
		 print('....')
	return task
#-------------------------------------------------------------------------------------------------------------------------
def command(task):
	task = task.split()
	if task[0] == "помоги":
		lbl.configure(text="обработка запроса")
		speak("[помоги] - выводит все команды\n"+
			"[найди] - ищет в интернете\n"+
			"[посчитай] - считает простые примеры(посчитай 2 + 2)\n"+
			"[открой] - открывает системное приложение(калькулятор, блокнот, ножницы)\n"+
			"[новости] - выводит популярные заголовки\n"+
			"[погода] - выводит нынещнюю погоду"+
			"[закрыть]  - закрывает меня")
	elif task[0] == "найди":
		lbl.configure(text="обработка запроса")
		web.open("https://yandex.ru/search/?text="+task[1]+"&lr=38&clid=218662")
	elif task[0] == "посчитай":
		if task[2] == "+":
			result = int(task[1]) + int(task[3])
			speak(result)
		if task[2] == "-":
			result = int(task[1]) - int(task[3])
			speak(result)
		if task[2] == "*":
			result = int(task[1]) * int(task[3])
			speak(result)
		if task[2] == "/":
			result = int(task[1]) / int(task[3])
			speak(result)
	elif task[0] == "открой":
		lbl.configure(text="обработка запроса")
		if task[1] == "калькулятор":
			os.system('calc')
		if task[1] == "блокнот":
			lbl.configure(text="обработка запроса")
			os.system("notepad")
		if task[1] == "ножницы":
			lbl.configure(text="обработка запроса")
			os.system('snippingtool')
	elif task[0] == "новости":
		lbl.configure(text="обработка запроса")
		url = "https://news.yandex.ru/"
		page = requests.get(url)
		soup = BeautifulSoup(page.text, "html.parser")
		for i in range(0,10):
			speak(soup.find_all(class_ = 'link link_theme_black i-bem')[i].getText())
	elif task[0] == "погода":
		url2 = "https://pogoda.mail.ru/prognoz/volgograd/"
		page2 = requests.get(url2)
		soup2 = BeautifulSoup(page2.text, "html.parser")
		lbl.configure(text="обработка запроса")
		speak("температура:"+soup2.find(class_ = "information__content__temperature").getText()+
			soup2.find(class_ = 'information__content__additional__item').getText()+
			"давление: " + soup2.find_all(class_ = 'information__content__additional__item')[2].getText()+
			"облачность: "+soup2.find_all(class_ = 'information__content__additional__item')[1].getText()+
			"влажность:"+soup2.find_all(class_ = 'information__content__additional__item')[3].getText()+
			"ветер:"+soup2.find_all(class_ = 'information__content__additional__item')[4].getText())
	elif task[0] == "закрыть":
		sys.exit()

	else:
		speak("команда не распонана")
#-------------------------------------------------------------------------------------------------------------------------
def spravka():
	root = Tk()
	root.title("справка")
	window.geometry('1000x800')

	lebal = Label(root, text="это справка")
	lebal.pack()
#-------------------------------------------------------------------------------------------------------------------------
def Lukas():
	command(record())
	#lbl.configure(text="упссссс....") 
#----------------------------------------------------------------------------------------------------------------------------
window = Tk()  
window["bg"] = "DeepSkyBlue3"
window.title("Лукас")  
window.geometry('1000x800')

btnspravka = Button(window, text="справка", bg="DeepSkyBlue3",fg="white",command=spravka)
btnspravka.place(x=0,y=0)
#btnspravka.grid(column=0, row=0)

lbl = Label(window, text = "Привет я голосовой ассистент Лукас", font = ("Arial Bold", 20), bg="DeepSkyBlue3"s, fg="white")
lbl.pack()
#lbl.grid(column = 0, row = 0)

image = ImageTk.PhotoImage(file = "luk3.png")
btn = Button(window, image = image, command = Lukas)#.pack()
btn.place(relx=.5, rely=.5, anchor="c", height=510, width=570, bordermode=OUTSIDE)
#btn.grid(column = 0, row = 1)
#btn.pack(side = RIGHT, padx=5, pady=5)
'''
btn = Button(window, text="Нажми чтобы начать", bg="blue", fg="white", command = Lukas)
btn.grid(column=1, row=0)
'''

window.mainloop()

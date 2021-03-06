from bot import telegram_bot

bot = telegram_bot("config.cfg")

def make_reply(msg):
    reply = None
    if msg == "/broker@tanyaTA_bot" or msg == "/broker":
        reply = "Kita pakai Maxrich Group (MRG), bisa daftar melalui link ini ya bit.ly/daftarbroker\n\nKalau bingung, udah kita buatin stepsnya di sini: https://www.instagram.com/s/aGlnaGxpZ2h0OjE3ODcxNjE0MDgwOTU0Mzc2?igshid=c8azcunq4fhm"
    elif msg == "/mt4@tanyaTA_bot" or  msg == "/mt4":
        reply = "https://www.youtube.com/watch?v=7KhEjJ3KDpo&t=1900s"
    elif msg == "/pemula@tanyaTA_bot" or  msg == "/pemula":
        reply = "Bisa daftar langsung ke link berikut bit.ly/freecourseTA. INI GRATIS! Setelah daftar nanti akan ada 4 video yang bisa ditonton dan 7 hari pembelajaran intensif ke email yang didaftarkan ya."
    elif msg == "/services@tanyaTA_bot" or  msg == "/services":
        reply = "1. *COMMANDO CENTER*, adalah program sinyal trading + edukasi secara tertulis. Sinyalnya untuk major currencies dan Gold ya.\nhttps://tradingacademy.id/homepage/commando-center/\n\n2. *MENTORSHIP PROGRAM*, program bimbingan selama satu tahun atau satu bulan, di mana Bapak  / Ibu akan belajar setiap hari dari senin hingga jumat tentang analisa teknikal dan psikologi dalam trading bersama mentor kami.\n(https://tradingacademy.id/mentorship/)\n\n3. *ONLINE COURSES*, adalah skill set yang merupakan pembelajaran secara mandiri dalam bentuk video, berkisar 30 hingga 45 menit tentang analisa teknikal. Tahapannya dari entry level (Battleplan), intermediate level (8 Trading Gates), ke advanced level (Price Action).\n(https://tradingacademy.id/courses/)"
    elif msg == "/contact@tanyaTA_bot" or  msg == "/contact":
        reply = "Chris_tradingacademyid - 0812 1999 5380 atau https://wa.me/message/QYUL4XNXA7NXK1"
    elif msg == "/help@tanyaTA_bot" or  msg == "/help":
        reply = "/broker@tanyaTA_bot - Broker yang kita pakai\n/mt4@tanyaTA_bot - Step by Step MetaTrader 4 (MT4)\n/pemula@tanyaTA_bot - Buat kamu yang baru mulai\n/services@tanyaTA_bot - Services yang diprovide tradingacademy.id\n/contact@tanyaTA_bot - Contact Person tradingcademy.id"
    return reply

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            checkNewMember = item["message"].get("new_chat_member")
            if checkNewMember:
                try:
                    firstname = str(item["message"]["new_chat_member"]["first_name"])
                except:
                    firstname = None
                #pcwelcome = item["message"]["new_chat_member"]["id"]
                pcwelcome = item["message"]["chat"]["id"]
                #welcomepc = "Welcome {}, perkenalkan saya Chris dari tim tradingacademy.id. Thank you sudah join dalam group diskusi yang kami buat ya,\n\nINI STARTER PACK UNTUK MEMULAI PERJALANAN TRADING KAMU: \n\n1. BUAT AKUN TRADING\nNah ini daftar broker dulu, kita pakai Maxrich Group (MRG), bisa daftar melalui link ini ya bit.ly/daftarbroker\n\n(Kalau bingung, udah kita buatin stepstepnya di sini bit.ly/stepbystepbroker)\n\n2. STEP BY STEP METATRADER 4\nbit.ly/tutorialmt4\n\n3. BASIC COURSE FOREX (GRATIS)\nLangsung ke link berikut bit.ly/freecourseTA. Setelah daftar nanti akan ada 4 video yang bisa ditonton dan 7 hari pembelajaran intensif ke email yang didaftarkan ya.\n\nTINGGAL DIIKUTIN SAJA STEP BY STEPNYA SUDAH BISA MULAI TRADING. Kalau ada apa apa, tinggal kontak saya di nomer 0812 1999 5380 (https://wa.me/message/QYUL4XNXA7NXK1) ini ya.\n\nLet the profit be with you 😊\nSalam tradingacademy.id".format(firstname)
                welcomepc = "Hi {}, welcome to this official group discussion dari tradingacademy.id! Kalo butuh apa apa, kamu bisa langsung ke @chris_tradingacademyid ya 😊".format(firstname)
                bot.send_message(welcomepc, pcwelcome)
            else:
                firstname = None
                
            if item["message"]["chat"]["id"] is not None:
                try:
                    message = str(item["message"]["text"])
                except:
                    message = None
                from_ = item["message"]["chat"]["id"]
                userid_ = item["message"]["from"]["id"]
                reply = make_reply(message)
                bot.send_message(reply, from_)
            elif item["message"]["chat"]["id"] is None:
                try:
                    message = str(item["message"]["text"])
                except:
                    message = None
                #from_ = item["message"]["chat"]["id"]
                userid_ = item["message"]["from"]["id"]
                reply = make_reply(message)
                bot.send_message(reply, userid_)
            #bot.send_message(reply, userid_)

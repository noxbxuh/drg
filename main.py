import telebot
from telebot import types
import random
import time

# ايدي القناة، الي تحب ينرسل بيها السؤال
id_ch = -1001998549970

# ضيف شكد متريد ادمنيه ،
user_admin = 5903160198,20875034,1025792859,6608312295,5703963661
mess_list = []  
#ضرغام 20875034
#ضرغام 5903160198
#كلاف 1025792859
#علاء 6608312295
#ليفه 5703963661

#ايديك
id_admin = 5903160198

#توكن بوتك
bot = telebot.TeleBot('7150275386:AAHFUi01vMRUUvfB2xvOJtDxVLSBcUYTeKo')

@bot.message_handler(commands=['info'])
def info(mes):
    with open('user_ursa.txt', 'r') as r:
        a = r.readlines()
        aa = len(a)
    with open('qbad.txt', 'r') as k:
    	kk = k.readlines()
    	fg = len(kk)
    with open('qlist.txt', 'r') as rg:
    	pf = rg.readlines()
    	jk = len(pf)
    	#ايديك تحت
    bot.send_message(id_admin, text=f'''
مرحبا سيدي .

المستخدمين : {aa}
الاسئله المقبوله : {jk}
الاسئله المرفوضه : {fg}
        ''')

userbot = 0

@bot.message_handler(commands=['start', 'URSA'])
def ursa(message):
    file = open('user_ursa.txt', "r").read()
    id = message.from_user.id
    name = message.from_user.full_name
    usern = message.from_user.username
    if str(id) not in file:
        with open('user_ursa.txt', 'a') as f:
            global userbot
            userbot += 1
            f.write(f'{userbot} - {id}\n')
        bot.send_message(id_admin,text='''

        ''')
    else:
        pass
        
    #غير يوزر قناة النشر
    u1 = types.InlineKeyboardButton('قناة النشر', url='t.me/CC22M')
    
    #يوزر قناتك
    u2 = types.InlineKeyboardButton('افضل بوتات التيليجرام', url='t.me/teamURSA')
    
    #يوزرك
    u3 = types.InlineKeyboardButton('المبرمج', url='t.me/d_xiim')
    u0 = types.InlineKeyboardMarkup()
    u0.add(u1)
    u0.add(u2)
    u0.add(u3)
    ee = bot.send_message(message.chat.id, text=f'''<strong>
    - اهلا بك عزيزي ،

- هذه البوت من صنع <s>أورسا - URSA </s> ،

- ارسل سؤالك و في حال مواقفة احد المشرفين سوف يتم نشر السؤال في القناة للحصول على المساعدة ،

- يجب ان لا يتجاوز 500 حرف ! .
    </strong>
            ''', parse_mode='html', reply_markup=u0)

@bot.message_handler(func=lambda message: True)
def forwar(message):
    global mess_list
    mess = message.text
    if len(mess) <= 500:
        u1 = types.InlineKeyboardButton('قناة النشر', url='t.me/CC22M')
        u2 = types.InlineKeyboardButton('افضل بوتات التيليجرام', url='t.me/teamURSA')
        u3 = types.InlineKeyboardButton('المبرمج', url='t.me/d_xiim')
        u0 = types.InlineKeyboardMarkup()
        u0.add(u1)
        u0.add(u2)
        u0.add(u3)
        bot.send_message(message.chat.id, text=f'''
- تم استلام سؤالك بنجاح ،

- انتظر موافقة احد المشرفين و سوف يتم نشر السؤال ،

- سؤالك : {mess}

- قناة النشر تحت .
        ''', reply_markup=u0)
        p1 = types.InlineKeyboardButton('موافقة ، نشر', callback_data=f'send_{len(mess_list)}')
        p2 = types.InlineKeyboardButton('رفض ، عدم النشر', callback_data=f'p2_{len(mess_list)}')
        p0 = types.InlineKeyboardMarkup()
        p0.add(p1, p2)
        name = message.from_user.full_name
        username = message.from_user.username
        id = message.from_user.id
        mess_list.append({'message': mess, 'id': id, 'username': username, 'name': name})
        for send_message_to_admin in user_admin:
            try:
            	bot.send_message(send_message_to_admin, text=f'''
- تم استلام سؤال جديد ،

- السؤال : {mess}

- العضو المرسل :
			- الاسم : {name}
			- اليوزر : @{username}
            	''', reply_markup=p0)
            except:
            	pass
    else:
        return bot.send_message(message.chat.id, text='- سؤالك طويل جدا !\n يجب ان لا يتجاوز 500 حرف .')

def send_mess(message_id):
    se = types.InlineKeyboardButton('ارسل سؤالك هنا .', url=f'https://t.me/URSA_1_bot?start={mess_list[message_id]["id"]}')
    ss = types.InlineKeyboardButton('الرد على العضو .', url=f't.me/{mess_list[message_id]["username"]}')
    es = types.InlineKeyboardMarkup()
    es.add(se)
    es.add(ss)
    bot.send_message(id_ch, text=f'''
- عضو يحتاج المساعده ،

- سؤال العضو : {mess_list[message_id]["message"]}
            ''', reply_markup=es)

@bot.callback_query_handler(func=lambda call: True)
def calll(call):
    message_id = int(call.data.split('_')[1])
    hh = open('qbad.txt', 'r').read()
    if call.data.startswith('send'):
        qlist = open('qlist.txt', 'r').read()
        if str(mess_list[message_id]["message"]) in qlist:
        	bot.answer_callback_query(callback_query_id=call.id, text='لقد تم نشر السؤال مسبقاً !')
        elif str(mess_list[message_id]["message"]) in hh:
        	bot.answer_callback_query(callback_query_id=call.id, text='لقد تم رفض السؤال هذه من قبل .')
        else:
        	send_mess(message_id)
        	bot.answer_callback_query(callback_query_id=call.id, text='تم نشر السؤال .')
        	with open('qlist.txt', 'a') as w:
        		w.write(f'{mess_list[message_id]["message"]}\n')
    
    elif call.data.startswith('p2'):
        idd = mess_list[message_id]["id"]
        qbad = open('qbad.txt', 'r').read()
        if str(mess_list[message_id]["message"]) in qbad:
        	bot.answer_callback_query(callback_query_id=call.id, text='لقد تم رفض السؤال مسبقا و اعلام العضو !')
        else:
        	with open('qbad.txt', 'a') as w:
        		w.write(f'{mess_list[message_id]["message"]}\n')
        	bot.send_message(idd, text=f'''
<strong>
- عذرا عزيزي العضو ،

- لقد تم رفض سؤالك من قِبل احد المشرفين ،

- راجع سؤالك او اكتبه بصيغه اخرى ثم عاود المحاولة لطفاً ،

السؤال : {mess_list[message_id]["message"]}
</strong>
        ''',parse_mode='html')

while True:
	def okk():
		try:
			bot.polling(True)
		except:
			time.sleep(5)
			okk()
		okk()
	okk()
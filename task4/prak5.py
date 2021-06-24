import http.client
import re
import telebot
import config
def maindata():
    conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': "06a132a9bbmsh4b2b32d05bbd0d5p1615f3jsn5cc43401ee3c",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }
    conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
    res = conn.getresponse()
    data = res.read()
    data1 = data.decode("utf-8")
    return data1
def getcases(st):
    data1 = maindata()
    if data1.find(st) != -1 and st != '':
        country = re.search(st, data1)
        pochcontr = country.start()
        data = data1[pochcontr:]
        cases = re.search('TotalCases', data)
        poch = cases.start()
        res = ''
        allres = ''
        s1 = True
        i = 0
        while s1 == True:
            if (data[i + poch] == ':'):
                i += 1
                while True:
                    if data[i + poch] == ',':
                        s1 = False
                        break
                    res += data[i + poch]
                    i += 1
                    allres = st + ' total cases: ' + res
            i += 1

    else:
        allres = 'incorrect data'
    return allres
bot = telebot.TeleBot(config.TOKEN)
@bot.message_handler(commands=['start'])
def a(message):
    bot.send_message(message.chat.id,'/help - справка')
@bot.message_handler(commands=['give5'])
def a(message):
    bot.send_message(message.chat.id,getcases('France') + '\n' + getcases('Russia') + '\n' + getcases('UK') + '\n' + getcases('Italy') + '\n' + getcases('Hungary'))
    text = '\n'+getcases('France') + '\n' + getcases('Russia') + '\n' + getcases('UK') + '\n' + getcases('Italy') + '\n' + getcases('Hungary')
    file=open('info.txt','a')
    file.write(text)
    file.close()
@bot.message_handler(commands=['help'])
def a(message):
    bot.send_message(message.chat.id, '/give5 - 5 країн\nдля пошуку окремих країн, надішліть мені назву країни з великої букви на англійській\n/save - створення файлу з історією\n/removedata - стирає історію')
@bot.message_handler(commands=['save'])
def a(message):
    file=open('info.txt','rb')
    bot.send_document(message.chat.id, file)
@bot.message_handler(commands=['removedata'])
def a(message):
    file = open('info.txt', 'w')
    file.write(' ')
    file.close()
    bot.send_message(message.chat.id,'видалено')
@bot.message_handler(content_types=['text'])
def a(message):
    mes = message.text
    if getcases(mes)!='incorrect data':
        bot.send_message(message.chat.id,getcases(mes))
        text='\n'+getcases(mes)
        file=open('info.txt','a')
        file.write(text)
        file.close()
    else:
        bot.send_message(message.chat.id, 'невірні дані')
bot.polling(none_stop=True)




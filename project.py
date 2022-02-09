import bs4
import requests
import telebot
from telebot import types

def pogoda():
    URL='https://ua.sinoptik.ua/погода-львів'
    HEADERS={'User Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
    response=requests.get(URL, headers=HEADERS)
    soup=bs4.BeautifulSoup(response.content, 'html.parser')
    for el in soup.select('#content'):
        #t_min=el.select('.temperature .min')[0].text
        #t_max=el.select('.temperature .max')[0].text
        day=el.select('.tabs .main')[0].text
        text=el.select('.wDescription .description')[0].text
        text_t = el.select(".weatherIco")[0].get("title")
        day1=el.select('.tabs .main')[1].text
        day2=el.select('.tabs .main')[2].text
        day3=el.select('.tabs .main')[3].text
        day4=el.select('.tabs .main')[4].text
        print(day+text_t+'\n'+text)
        #print(day1)
        #print(day2)
        #print(day3)
        #print(day4)

    Token='1786599612:AAHpo5v0Bh8NYnxuF-F9ki9oepMMcHZ2gFg'
    bot=telebot.TeleBot(Token)

    @bot.message_handler(commands=['start', 'help'])
    def main(message):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Сьогодні")
        item2=types.KeyboardButton("Завтра")
        item3=types.KeyboardButton("На 5 днів")
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, "Привіт, погода:", reply_markup=markup)
    
    @bot.message_handler(content_types=['text'])    
    def message(message):
        if message.chat.type == 'private':
            if message.text == 'Сьогодні':
                bot.send_message(message.chat.id, day+text_t+'\n'+text)
            elif message.text == 'Завтра':
                bot.send_message(message.chat.id, day1)
            else:
                bot.send_message(message.chat.id, day+'\n'+day1+'\n'+day2+'\n'+day3+'\n'+day4)
        
    bot.polling(none_stop=True)
           
        
pogoda()

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import setting

logging.basicConfig (format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

#
#

#PROXY -названа БОЛЬШИМИ буквами, т.к. не должна меняться в процессе работы программы.
#Такие переменные менять НЕЛЬЗЯ!

def greet_user(boat, update):
    text='Вызван /start'
    print(text)
    update.message.reply_text(text)

def talk_to_me(boat, update):
    user_text='Привет {}! Ты написал: {}'.format(update.message.chat.first_name, update.message.text)
    print(user_text)   
    print(update.message) 
    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.username, 
                update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def main(): 
    #- объявление функции
    mybot=Updater(setting.API_KEY) 
    #API ключ от BotFather

    logging.info('Бот запускается')

    dp=mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()

main()
#- вызов функции, т.е она начинает делать то, что прописали при объявлении функции


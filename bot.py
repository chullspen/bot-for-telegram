from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json
updater = Updater(token="824890757:AAEPDkfEFMzucc14fbXnHso45fsRIids7FM")
dispatcher = updater.dispatcher

# обработка команд
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Привет, давай пообщаемся.")

def textMessage(bot, update):
    request = apiai.ApiAI("f27524fc061a4063bcd9263676a038a4").text_request() #Токен API к DialogFlow
    request.lang = 'ru'
    request.session_id = 'OhHiDimaBot'
    request.query = update.message.text
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    if response:
        bot.send_message(chat_id=update.message.chat_id, text=response)

    else:
        bot.send_message(chat_id=update.message.chat_id, text="Я вас не понял")

# Хендлеры 
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling(clean=True)

updater.idle()
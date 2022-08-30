import telebot
from telebot import types
from gtts import gTTS


bot = telebot.TeleBot('5493591819:AAFQgTNpfOG6cJn7hAT-y8sgVfqoOyBokZE')


def text_to_speech(s):
    mytext = s
    language = 'ru'
    myobj = gTTS(text = mytext, lang = language, slow = False)
    myobj.save('v.mp3')
    pass




@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Сейчас все озвучу, введите то, что необходимо озвучить")
    else:
        markup = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("Озвучить", callback_data='озвучить')
        markup.add(item1)
        bot.send_message(message.from_user.id, text =message.text, reply_markup = markup)


#нажатие на клавишу
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'озвучить':
        msg = text_to_speech(call.message.text)
        file = open('v.mp3', 'rb')
        bot.send_audio(call.message.chat.id, file)


bot.polling(none_stop=True, interval=0)



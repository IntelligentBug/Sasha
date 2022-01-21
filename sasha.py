import telebot

# from telebot import apihelper
# apihelper.proxy = {
#     'https':'socks5://login:password@ip:port'}


token = "5096756308:AAETy41R7MFwGv_xD5_oeRc3Qj6WlSlQhJg"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Hello', 'Bye')
    bot.send_message(message.chat.id, 'Hello!', reply_markup=keyboard)


@bot.message_handler(commands=['test'])
def start_message2(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(
        text='Three', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(
        text='Four', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(
        text='Five', callback_data=5))
    bot.send_message(
        message.chat.id, text="How much is 2 plus 2?", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, 'Hello again!')
    elif message.text.lower() == 'bye':
        bot.send_message(message.chat.id, 'Bye!')


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(
        callback_query_id=call.id, text='Answer accepted!')
    answer = 'You made a mistake'
    if call.data == '4':
        answer = 'You answered correctly!'

    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(
        call.message.chat.id, call.message.message_id)


bot.polling()

import telebot
import random
bot = telebot.TeleBot("")
#bot.send_message(153076386,"test")
@bot.message_handler(content_types= ['text'])
def handle_command(message):
         x=message.text
         r=random.randrange(0, 11, 1)
         femp=['ница','ка','иса','ая','ьша','ша','ица','есса','ша','иха','щица','иня']
         bot.send_message(message.chat.id, x+femp[r])
#message.chat.id возвращает код чата с конкретным пользователем (мы не знаем заранее его ID)

bot.polling(none_stop=True, interval=0)
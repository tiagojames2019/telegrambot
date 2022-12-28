import telebot
import os
import dotenv
dotenv.load_dotenv()
token = os.getenv('autorization')
bot = telebot.TeleBot(token)

#Funções
#Enviar mensagem 
#bot.send_message(mensagem.chat.id,)
#bot.reply_to(mensagem, texto)

def verificar(mensagem):
    return True

#Decorator
@bot.message_handler(commands=['btc'])
def btc(mensagem):
    bot.send_message(mensagem.chat.id, "Cotação Atual é R$ 87.297")

#Decorator
@bot.message_handler(commands=['petr4'])
def btc(mensagem):

    bot.send_message(mensagem.chat.id, "Cotação Atual é R$ 24,98")

#Decorator
@bot.message_handler(func=verificar)
def responder(mensagem):
    
    texto = f"""
    Olá {mensagem.chat.first_name} qual ação gostaria de saber o preço
    /btc
    /petr4
    """
    bot.reply_to(mensagem, texto)

#loop infinito para ler mensagem 
bot.polling()

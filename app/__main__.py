import sys
sys.path.append('./bot/hnd/')

from handler import TelegramBot
bot = TelegramBot("1294503101:AAEJl5Nvsrmijouu-rDiBJHJtw9crJiHU0g")


@bot.command("start")
def start(bot, context):
    bot.message.reply_text("Используемые команды:\n!creation (file.txt) (info)\n!read (file.txt)\n!add (file.txt) (info)!")


@bot.prefix(["!"],"creation")
def creation_file (bot, context):
    name, text = context.args[0], " ".join(context.args[1:],)
    with open("{}".format(str(name)), 'tw', encoding='utf-8') as file:
        file.write(str(text)+'\n')


@bot.prefix(["!"], "read")
def read_file (bot, context):
    name = context.args[0]
    with open(name, "r",) as file:
        result = file.read()
        bot.message.reply_text(result)


@bot.prefix(["!"], "add")
def add_file (bot, context):
    name, text = context.args[0], " ".join(context.args[1:],)
    with open("{}".format(str(name)), "a") as file:
        file.write(text)
    
bot.run()
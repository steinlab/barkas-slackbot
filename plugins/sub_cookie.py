from . import bot


@bot.subscribe('cookie')
@bot.subscribe('пиши')
def sub_cookie(message):
    bot.speak('Я записала "{0}"'.format(message))
    with open('/home/steinlab/dev/slackbot/tags.txt', mode='a', encoding='utf-8') as myfile:
        myfile.write(message + '\n')
        myfile.close()




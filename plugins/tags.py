from . import bot
import re

@bot.firehose
def listen(tag):
    # Attempt to strip out URLs
    #tag = re.sub('(https?|ftp)://\S+', '', tag)
    pattern = "#"
    m = re.search(pattern, tag, re.IGNORECASE)
    if m:
        bot.speak("Думаю...")
        file = open('/home/steinlab/dev/slackbot/tags.txt', mode='a', encoding='utf-8')
        file.write(tag + '\n')
        file.close()
        #image = 'http://i.imgur.com/9Zv4V.gif'
        bot.speak("Текст добавлен")

#@bot.firehose
#def listenMessage(message):
#    pattern = '!заметка'
#    n = re.search(pattern, message, re.IGNORECASE)
#    message = re.sub(pattern, '', message)
#    if n:
#        file = open('/home/steinlab/dev/slackbot/tags.txt', mode='a', encoding='utf-8')
#        file.write(message + '\n')
#        file.close()
#        #image = 'http://i.imgur.com/9Zv4V.gif'
#        bot.speak("Текст добавлен")

@bot.firehose
def readMessage(request):
    pattern = '!read'
    n = re.search(pattern, request, re.IGNORECASE)
    request = re.sub(pattern + ' ', '', request)
    if n:
        bot.speak("Думаю...")
        file = open('/home/steinlab/dev/slackbot/tags.txt', mode='r', encoding='utf-8')
        for line in file:
            file.readline()
            if request in line:
                bot.speak("Результат поиска: %s" % line.strip())
        file.close()










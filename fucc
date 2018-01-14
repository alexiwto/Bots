import tweepy
import tweepy, time
from tweepy import OAuthHandler
from random import randint

fuck = 'fucc '
palabro = ''
fuckpalabro = ''
palabras = []
consumer_key = 'ZNWYFFR07TlyRydvE2OdOAFEb'
consumer_secret = 'mDIw8exelAcSWev83d0JfibelI6SAdBjY7sVRnFjnw4TcXYbms'
access_token = '951760098879209472-hMPIKjmtkql6WHbiO3S6LOJJhDrTqp4'
access_secret = 'cvuc0xHfGYWCAF3o0seizBGXwYBpFFU9NaPH0u8z8CJmD'


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
tweetBot = tweepy.API(auth)

def palabraRandom():
        with open('/root/python/palabrasIngles.txt', 'r', encoding='utf-8') as file:
                for palabra in file:
                        palabras.append(palabra)
        file.close()
        numeroRandom = randint(0, len(palabras)-1)
        return palabras[numeroRandom]




palabro = palabraRandom().replace("\n", "")
fuckpalabro = (fuckpalabro.join([fuck,palabro]))


tweetBot.update_status(fuckpalabro)

import tweepy
import tweepy, time
from tweepy import OAuthHandler
from random import randint

fuck = 'fucc '
palabro = ''
fuckpalabro = ''
palabras = []

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
tweetBot = tweepy.API(auth)

def palabraRandom():
        with open('palabrasIngles.txt', 'r', encoding='utf-8') as file:
                for palabra in file:
                        palabras.append(palabra)
        file.close()
        numeroRandom = randint(0, len(palabras)-1)
        return palabras[numeroRandom]




palabro = palabraRandom().replace("\n", "")
fuckpalabro = (fuckpalabro.join([fuck,palabro]))


tweetBot.update_status(fuckpalabro)

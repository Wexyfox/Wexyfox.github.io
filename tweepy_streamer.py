from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
#required tweepy modules

from textblob import TextBlob
#import textblob

import twitter_credentials
#holds all the keys for the API access

import re
import joblib
import nltk

def classify(sentence):
    classifier = joblib.load("model.pkl")

    def preprocessor(sentence):
        sentence = sentence.strip().lower()
        sentence = re.sub(r"\d+", "", sentence)
        sentence = re.sub(r'[^\w\s]', '', sentence)
        sentence = " ".join([w for w in nltk.word_tokenize(sentence) if len(w) > 1])

        return sentence

    clean_data = [preprocessor(sentence)]
    vec = joblib.load("vectorizer.pkl")
    data_text_sparse = vec.transform(clean_data)

    prediction = classifier.predict(data_text_sparse)[0]

    return prediction


class MyTweetStreamer():
    #class for filtering tweets

    def __init__(self):
        pass

    def stream_tweets( self ):
    #authenticates and connects to the Twitter Streaming API

        listener = OutListener()

        #creates object of the class which inherits the StreamListener

        authenticator = OAuthHandler( twitter_credentials.CONSUMER_KEY , twitter_credentials.CONSUMER_SECRET )
        authenticator.set_access_token( twitter_credentials.ACCESS_TOKEN , twitter_credentials.ACCESS_TOKEN_SECRET)
        #authenitcaes the code using the keys

        stream = Stream( authenticator , listener )
        #variable that holds the imported Stream

        stream.filter( track = ['#news'] )
        #only picks up tweets containing hashtag as apposed to all tweets and then filtering


class OutListener(StreamListener):
    #class for the basic listener that passes recieved tweets from the API

    #constructor
    def __init__(self):

        pass

    def on_data( self , data ):
        #writes tweets to the text file

        global num_tweets
        #allows for manipulation of counter in the constant stream

        try:
            #print(data)
            language_start_point = data.find(',"lang":"') + len(',"lang":"')
            language_end_point = data.find('","timestamp_ms":"')
            tweet_langauge = data[language_start_point : language_end_point]


            if tweet_langauge == "fr":
            #finds the tweet language and only continues if it is the specified language
                text_start_point = data.find(',"text":"') + len(',"text":"')
                text_end_point = data.find(',"source":"')
                tweet_text = data[text_start_point : text_end_point]

                if tweet_text[:4] != "RT @":
                #finds the tweet text and only continues if it is not a retweet (broken up text from streamer)

                    num_tweets += 1
                    #checks if the number of tweets meets the required amount and breaks out

                    if num_tweets == 2:
                        print(tweet_text)
                        list_tweets.append(tweet_text)
                        exit()
                    else:
                        print(tweet_text)
                        list_tweets.append(tweet_text)
                        return True


        #prints error to command line if an error is encounted
        except BaseException as e:
            print("Error on_data: %s" % str(e))

            if str(e) == "None":
            #if the break was initiated because the required amount of tweets is aquired
                for tweet in list_tweets:
                    tweet = TextBlob(tweet)
                    translated_tweet = tweet.translate( to = "en" )
                    #print(translated_tweet)
                    prediction = classify(translated_tweet)
                    list_translations.append(translated_tweet , prediction)

                print(list_translations)
            exit()

        return True

    def on_error( self , status ):
        print(status)
        #prints status if an error is encounted

if __name__ == "__main__":
    #standard sanity check
    num_tweets = 0
    list_tweets = []
    list_translations = []

    twitter_streamer = MyTweetStreamer()
    twitter_streamer.stream_tweets()

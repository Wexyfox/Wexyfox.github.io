from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
#required tweepy modules

import twitter_credentials
#holds all the keys for the API access


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

        stream.filter( track = ['#corona'] )
        #only picks up tweets containing hashtag as apposed to all tweets and then filtering


class OutListener(StreamListener):
    #class for the basic listener that passes recieved tweets from the API

    #constructor
    def __init__(self):
        pass

    def on_data( self , data ):
        #writes tweets to the text file
        try:
            #print(data)
            language_start_point = data.find(',"lang":"') + len(',"lang":"')
            language_end_point = data.find('","timestamp_ms":"')
            tweet_langauge = data[language_start_point : language_end_point]

            if tweet_langauge == "fr":
                text_start_point = data.find(',"text":"') + len(',"text":"')
                text_end_point = data.find(',"source":"')
                tweet_text = data[text_start_point : text_end_point]
                if tweet_text[:4] != "RT @":
                    print(tweet_text)
                    with open( "tweets.txt" , 'a') as tf:

                        tf.write( str(num_tweets) + " " + tweet_text + "\n" )
                        num_tweets = num_tweets + 1
                        return True

        #prints error to command line if an error is encounted
        except BaseException as e:
            print("Error on_data: %s" % str(e))

        return True

    def on_error( self , status ):
        print(status)
        #prints status if an error is encounted

if __name__ == "__main__":
    #standard sanity check
    num_tweets = 0

    twitter_streamer = MyTweetStreamer()

    while num_tweets != 10
        twitter_streamer.stream_tweets()

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
#required tweepy modules

import twitter_credentials
#holds all the keys for the API access


class MyTweetStreamer():
    #class for filtering tweets

    def stream_tweets( self , fetched_tweets_filename ):
    #authenticates and connects to the Twitter Streaming API

    listener = OutListener()
    #creates object of the class which inherits the StreamListener

    authenticator = OAuthHandler( twitter_credentials.CONSUMER_KEY , twitter_credentials.CONSUMER_SECRET )
    authenticator.set_access_token( twitter_credentials.ACCESS_TOKEN , twitter_credentials.ACCESS_TOKEN_SECRET)
    #authenitcaes the code using the keys

    stream = Stream( authenticaor , listener )
    #variable that holds the imported Stream

    stream.filter( track = ['#construction'] )
    #only picks up tweets containing hashtag as apposed to all tweets and then filtering


class OutListener(StreamListener):
    #class for the basic listener that passes recieved tweets from the API

    def __init__( self , fetched_tweets_filename):
    #constructor that allows the class to be made an object which is associated with a file that it is writing to
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data( self , data ):
        #tries to
        try:
            with open( self.fetched_tweets_filename , 'a') as tf:
                tf.write( data )
            return True

        except BaseException as e:
            print("Error on_data: %s" % str(e))

        return True

    def on_error( self , status ):
        print(status)
        #prints status if an error is encounted

if __name__ == "__main__":
    #standard sanity check
    fetched_tweets_filename = "tweets.json"

    twitter_streamer = MyTweetStreamer()
    twitter_streamer.stream_tweets( fetched_tweets_filename )

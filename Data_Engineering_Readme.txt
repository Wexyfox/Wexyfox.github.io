Welcome to Atradius' Data Engineer Interview Process!

One of the many different data driven projects and proof-of-concepts we do at Atradius, 
is that of measuring the general sentiment levels towards companies Atradius has exposure to. 
This helps Atradius stay on top of future risks, by monitoring whether a company is suddenly 
getting a lot of negative reviews on, for example, social media.
For your take-home task, we reduce this problem to the simple task of sentence-based sentiment classification. 

The classifier model has been provided for you and it is your task as the data engineer to 
source the necessary data to feed the model and to store the resulting model outputs.

Please note that the test is not so much about finishing and solving the problem, but about 
delivering a well designed
solution with code and documentation in good quality. Because we are mainly working with 
Python/R we would like you to do this in Python or R.

Task 1:
Stream Twitter Tweets
- You must register a developer account with twitter and utilise their streaming api endpoint 
(hint: Tweepy (python) or twitteR (R) could be useful libraries) to gather 100 tweets with the 
hashtag: #construction
  The tweets must be in a language that is not English (the twitter api has both geocode and language parameters).
- Using an opensource translation library (e.g. textblob) the streamed tweets must be translated to English.
- The translated tweets must then be passed to the model script provided. This script contains 
a function that takes a sentence string as input and outputs a sentiment label, either "positive", 
"negative" or "neutral".

Task 2:
Data Storage
- Save the model results to a .JSON file 
- Lastly, programatically retrieve the following information based on your dataset: Total counts 
for each sentiment category

You must return all your code, the pipeline should do as follows:
- Stream tweets
- Translate tweets
- Input tweets in to provided classifier
- Save the results in a JSON file
- Provide basic information on compiled results

We will run your code, so make sure it can be run without too many changes

If your solution qualifies, on the day of the interview we would like you to present your solution 
and code to us, and rationalize the choices you have made in order to achieve your results.
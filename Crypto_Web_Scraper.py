def outputindividualtweet():

    # import libraries
    import tweepy
    from textblob import TextBlob

    # The information we need to use twitter's api, get from dev account
    consumer_key = "x"
    consumer_secret = "x"
    access_token = "x"
    access_token_secret = "x"

    # Setting up twitter API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Our keyword
    keyword = 'Bitcoin'

    # Search tweets for keyword
    public_tweets = api.search(keyword)

    # Print the tweet and the sentiment anaylsis of that tweet
    for tweet in public_tweets:
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)


def outputtotalvalue():
    # import libraries
    import tweepy
    from textblob import TextBlob

    # The information we need to use twitter's api, get from dev account
    consumer_key = "x"
    consumer_secret = "x"
    access_token = "x"
    access_token_secret = "x"

    # Setting up twitter API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Our keyword
    keyword = 'Bitcoin'

    # Search tweets for keyword
    public_tweets = api.search(keyword)

    polarity = 0
    subjectivity = 0
    counter = 0

    # Print the tweet and the sentiment anaylsis of that tweet
    for tweet in public_tweets:
        # print(tweet.text)
        analysis = TextBlob(tweet.text)
        # print(analysis.sentiment)
        polarity += analysis.sentiment[0]
        subjectivity += analysis.sentiment[1]
        counter += 1

    emotion = int((polarity / counter) * 100)
    subjectiveness = int((subjectivity / counter) * 100)

    print("Polarity: ", str(emotion) + "%", " | Subjectivity: ", str(subjectiveness) + "%")

    if emotion > 0:
        print("IT'S GOING UP. BUY! BUY! BUY!")
    else:
        print("IT'S GOING DOWN. SELL! SELL! SELL!")

outputtotalvalue()

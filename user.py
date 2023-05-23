import tweepy

# API-Zugangsdaten
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

# Authentifizierung bei der API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Bildschirmname des Twitter-Profils
screen_name = "twitter_handle"

# Anfrage an den Endpunkt "users/show"
user = api.get_user(screen_name)

# Anfrage an den Endpunkt "statuses/user_timeline" für die letzten 200 Tweets des Benutzersm, könnt ihr beliebig erhöhen.
tweets = api.user_timeline(screen_name=screen_name, count=200)

# Ausgabe der vergangenen Usernamen und der Twitter ID
print("Vergangene Usernamen für @" + screen_name + ":")
for username in user._json['entities']['user_mentions']:
    print(username['screen_name'])
print("Twitter ID für @" + screen_name + ": " + str(user.id))

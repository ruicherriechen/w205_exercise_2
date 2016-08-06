import tweepy

consumer_key = "2sY9TWQKtpIwF3mLDnUITLZ7S";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "EpvW9OXnb29bXjE2OxiGXMxuBeb9Ar5SjRnDJwl7Iv8kIuTOIg";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "2282318802-9HL8UYn4MLwwOWiriKXSPEzHUZP2E4qbIYXH0tJ";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "YlMsXuvdiqbdpUaDu0bR8yGiMQXCE02uu1insimA2hBt6";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)




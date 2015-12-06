import tweepy

consumer_key = "CDPJ2cCoN1s5s3q2NZJgRy0au";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "dCGHtQHCaY0tfxR0IH0545HGz3rZLgCRjmFjsITwtdj0A1nSRo";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "7545822-1NKFqwL31JXePMKfpOHTyaJDn28dA9tOcbQpxiK33z";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "jn5lhaikadBmb1ocwAY3pedXLosiBOCsaBOYWMa9065XW";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)




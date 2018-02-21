import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = {
    "consumer_key"        : 'YrmtAW959j42Wke15OgcKdd2Z',
    "consumer_secret"     : 'jRsPdpXqQdCKrQ4aoerRvk4EuqsN4S6ZXMDFgS1Up7WvtBDJux',
    "access_token"        : '966150844797407232-1p3fFiPLRMPTbUD4hTuEwmjEUV6LSWf',
    "access_token_secret" :  '3MaOheHXKFPViLFjSqkjmCHdwAarstAQR1hvszol77uiX'
    }

  api = get_api(cfg)
  tweet = "Hello, world!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()

import re

def omit_hashtag(message, hashtag):
    return re.sub(hashtag, '', message, count = 1)

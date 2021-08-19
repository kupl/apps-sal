def generate_hashtag(s):
    hashtag = '#' + ''.join((word.capitalize() for word in s.split()))
    return hashtag if 1 < len(hashtag) <= 140 else False

def generate_hashtag(s):
    hashtag = "#"+"".join(i.title() for i in s.split())
    return hashtag if s and len(hashtag) <= 140 else False

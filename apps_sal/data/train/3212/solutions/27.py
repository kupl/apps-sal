def generate_hashtag(s):
    return False if len(s) > 140 or not s.split() else '#' + ''.join(map(lambda x: x.capitalize(), s.split()))

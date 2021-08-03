def generate_hashtag(s):
    return False if (s == '' or len(s) > 140) else '#' + ''.join(s.title().split())

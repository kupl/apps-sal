def generate_hashtag(s):
    s = '#' + ''.join(s.title().split())
    return [s if 1 < len(s) < 140 else False][0]

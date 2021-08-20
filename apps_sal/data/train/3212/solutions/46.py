def generate_hashtag(s):
    return '#' + s.title().replace(' ', '') if s and len(s) < 140 else False

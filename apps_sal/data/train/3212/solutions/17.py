def generate_hashtag(s):
    return '#'+ s.lower().title().replace(' ', '') if 141 > len(s) > 0 else False

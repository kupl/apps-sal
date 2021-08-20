def generate_hashtag(s):
    return ('#' + s.title().replace(' ', '') if len('#' + s.title().replace(' ', '')) <= 140 else False) if len(s) != 0 else False

def generate_hashtag(s):
    return '#' + s.title().replace(' ', '')if not s.isspace() and 0 < len(s) <= 140 else False

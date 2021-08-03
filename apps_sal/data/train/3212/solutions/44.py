def generate_hashtag(s):
    if s == '' or len(s) > 140:
        return False
    return '#' + s.title().strip().replace(' ', '')

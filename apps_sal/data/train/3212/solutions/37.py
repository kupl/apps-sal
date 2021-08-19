def generate_hashtag(s):
    s = str(s).title()
    if s == '':
        return False
    if len(s) > 144:
        return False
    return '#' + s.replace(' ', '')

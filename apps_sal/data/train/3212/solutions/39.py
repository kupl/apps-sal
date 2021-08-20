def generate_hashtag(s):
    if not s:
        return False
    s = s.title().replace(' ', '')
    if not s or len(s) > 139:
        return False
    return '#' + s

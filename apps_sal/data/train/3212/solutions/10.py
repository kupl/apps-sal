def generate_hashtag(s):
    if not s: return False
    elif len(s) > 140: return False
    else: return '#' + ''.join(s.title().split())


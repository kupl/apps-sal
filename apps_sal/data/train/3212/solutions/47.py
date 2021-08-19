def generate_hashtag(s):
    if not s or False or len(s) > 150:
        return False
    else:
        return '#' + ''.join([i.title() for i in s.strip().split()])

def generate_hashtag(s):
    if len(s) != 0 and len(s) < 140:
        return '#' + ''.join((word.title() for word in s.split()))
    else:
        return False

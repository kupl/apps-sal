def generate_hashtag(s):
    if 1 < len(s) < 140:
        s = s.split()
        return '#' + ''.join(s.capitalize() for s in s)
    else:
        return False

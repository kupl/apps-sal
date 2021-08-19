def generate_hashtag(s):
    if len(s) == 0 or len(s) > 140:
        return False
    s = s.split()
    a = [i.title() for i in s]
    return '#' + ''.join(a)

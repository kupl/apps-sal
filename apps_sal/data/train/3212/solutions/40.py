import string


def generate_hashtag(s):
    if len(s) == 0 or len(s) > 140:
        return False
    else:
        y = ''.join((string.capwords(s)).split(' ', (string.capwords(s)).count(' ')))
        m = '#' + y
        return m

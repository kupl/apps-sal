def generate_hashtag(s):
    ans = '#' + str(s.title().replace(' ', ''))
    return s and (not len(ans) > 140) and ans or False

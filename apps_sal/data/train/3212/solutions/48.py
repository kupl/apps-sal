def generate_hashtag(s):
    s_arr = s.title().split(' ')
    hashtag = '#' + ''.join(s_arr)
    if len(hashtag) > 140 or len(hashtag) < 2:
        return False
    else:
        return hashtag

def generate_hashtag(s):
    return '#{}'.format(s.title().replace(' ', '')) if len(s) in range(1, 141) else False

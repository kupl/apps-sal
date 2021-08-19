def generate_hashtag(s):
    s = ''.join((i.capitalize() for i in s.split()))
    return f'#{s}' if len(s) < 140 and s.isalpha() else False

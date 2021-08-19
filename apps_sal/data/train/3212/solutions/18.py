def generate_hashtag(s):
    answer = '#' + ''.join([i.capitalize() for i in s.split()])
    return False if not s or len(answer) > 140 else answer

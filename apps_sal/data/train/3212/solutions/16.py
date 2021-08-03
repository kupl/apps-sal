def generate_hashtag(s):
    if s == '' or len(s) > 140:
        return False
    return '#' + "".join([i.capitalize() for i in s.split(' ')])

def generate_hashtag(str):
    return '#' + ''.join(word.capitalize() for word in str.split(' ')) if str and len(str) < 140 else False

def generate_hashtag(s):
    # your code here
    if len(s) != 0 and len(s) < 140:
        return '#' + ''.join(word.title() for word in s.split())
    else:
        return False

def generate_hashtag(s):
    if not len(s):
        return False
    s = "#" + s.title().replace(" ", "")
    return s if len(s) <= 140 else False

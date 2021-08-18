def generate_hashtag(s):
    nword = "
    if s == "":
        return False
    elif len(s) > 140:
        return False
    else:
        for word in s.split():
            nword += word.capitalize()
        return nword

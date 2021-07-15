def generate_hashtag(s):
    if not s:
        return False

    if len(s) > 140:
        return False

    result = "#"
    for word in s.split():
        result += word[0].upper() + word[1:].lower()

    return result

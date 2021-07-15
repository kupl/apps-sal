def generate_hashtag(s):
    if len(s) > 140: return False
    if len(s) == 0: return False
    return f"#{''.join([x.capitalize() for x in s.split()])}"


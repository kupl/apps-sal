def generate_hashtag(s):
    return f"#{s.title().replace(' ', '')}" if 0 < len(s) <= 140 else False

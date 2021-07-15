def generate_hashtag(s):
    return 0 if not s or len(s)>140 else f'#{"".join(e for e in s.title().split())}'

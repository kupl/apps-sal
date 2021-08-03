def generate_hashtag(s): return '#' + s.strip().title().replace(' ', '') if 0 < len(s) <= 140 else False

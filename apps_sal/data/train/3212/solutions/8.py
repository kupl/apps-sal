def generate_hashtag(s):
    if len(s) > 140 or not s: return False 
    return '#' + ''.join(w.capitalize() for w in s.split())

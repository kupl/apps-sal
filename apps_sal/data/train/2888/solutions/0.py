def remove(s):
    return ' '.join(w.rstrip('!') or w for w in s.split())

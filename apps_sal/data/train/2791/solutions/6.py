def trigrams(s):
    return ' '.join([''.join(w).replace(' ', '_') for w in list(zip(s, s[1:], s[2:]))]) if len(s) > 2 else ''

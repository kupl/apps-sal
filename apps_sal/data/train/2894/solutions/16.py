def triple_trouble(r, s, t):
    return ''.join([c + s[i] + t[i] for (i, c) in enumerate(list(r))])

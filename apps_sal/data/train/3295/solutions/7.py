def split_in_parts(s, p):
    return ' '.join([s[i:i + p] for i in range(0, len(s), p)])

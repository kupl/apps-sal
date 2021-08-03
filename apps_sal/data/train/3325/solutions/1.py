def most_common(s):
    return ''.join(sorted(s, key=s.count, reverse=True))

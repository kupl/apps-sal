def most_common(s):
    return ''.join(sorted(s, key=lambda i: -s.count(i)))

def most_common(s):
    T = sorted(s, key=lambda x: -s.count(x))
    return ''.join(T)

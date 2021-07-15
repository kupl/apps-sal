def most_common(a):
    return ''.join(sorted(a, key = a.count, reverse = True))

def rankings(a):
    return sorted(range(1, len(a) + 1), key=([0] + sorted(range(len(a)), key=a.__getitem__, reverse=1)).__getitem__)

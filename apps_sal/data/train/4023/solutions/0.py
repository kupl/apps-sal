def high(x):
    return max(x.split(), key=lambda k: sum((ord(c) - 96 for c in k)))

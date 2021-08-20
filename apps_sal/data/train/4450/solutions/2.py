def consecutive(a):
    return len(a) and -~max(a) - min(a) - len(a)

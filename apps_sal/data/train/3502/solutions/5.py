def solution(*args):
    s = set()
    for x in args:
        if x in s:
            return 1
        s.add(x)
    return 0

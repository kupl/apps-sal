def find_missing_number(s):
    if len(s) < 1: return 0
    try:
        s = sorted(int(x) for x in s.split())
    except:
        return 1
    for c, x in enumerate(s, 1):
        if c != int(x):
            return c
    return 0

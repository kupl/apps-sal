def find_missing_number(s):
    s = s.split()
    if not all(x.isdigit() for x in s): return 1
    r = range(1, len(s) + 1)
    for x in r:
        if str(x) not in s: return x
    return 0

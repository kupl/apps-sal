def solve(s):
    big = 0
    small = 0
    for x in s:
        if 65 <= ord(x) <= 90:
            big += 1
        else:
            small += 1
    return s.lower() if small >= big else s.upper()

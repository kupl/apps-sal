def solve(st):
    for i in range(len(st) - 1, 0, -1):
        if not i or (len(st) >= 2 * i and st[0:i] == st[-i:]):
            return i
    return 0

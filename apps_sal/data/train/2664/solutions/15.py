def solve(s):
    r = [s[i] != s[len(s) - 1 - i] for i in range(len(s) // 2)]
    if len(s) % 2:
        return True if sum(r) < 2 else False
    else:
        return True if sum(r) == 1 else False

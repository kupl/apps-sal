from functools import partial


def check(s, tail):
    i = s.find(tail[1])
    if i == -1:
        return float('inf')
    s = s[:i] + s[i + 1:]
    j = s.find(tail[0])
    if j == -1:
        return float('inf')
    s = s[:j] + s[j + 1:]
    if not s:
        return i + j
    if s == '0' * len(s):
        return float('inf')
    return i + j + next((i for (i, c) in enumerate(reversed(s)) if c != '0'))


def solve(n):
    result = min(map(partial(check, str(n)[::-1]), ('00', '25', '50', '75')))
    return -1 if result == float('inf') else result

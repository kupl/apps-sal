def solve(a):
    return list(dict.fromkeys(reversed(a)))[::-1]

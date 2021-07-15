def solve(s):
    fs = [str.isupper, str.islower, str.isdigit]
    res = [0, 0, 0, 0]
    for c in s:
        res[next((i for i, f in enumerate(fs) if f(c)), -1)] += 1
    return res

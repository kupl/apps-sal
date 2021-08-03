def solve(s):
    val = [90 - ord(c) for c in reversed(s)]
    tmp, res = [0], val[0]
    for v1, v2 in zip(val, val[1:]):
        tmp.append(tmp[-1] * 26 + v1)
        res += v2 * (tmp[-1] + 1)
    return res % (10**9 + 7)

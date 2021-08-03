def solve(s):
    r = s[::-1]
    i = next((i for i, (c1, c2) in enumerate(zip(s, r)) if c1 != c2), None)
    if i is None:
        return 'OK'
    j = len(s) - i
    if s[i + 1:] == r[i:j - 1] + r[j:] or s[i:j - 1] + s[j:] == r[i + 1:]:
        return 'remove one'
    else:
        return 'not possible'

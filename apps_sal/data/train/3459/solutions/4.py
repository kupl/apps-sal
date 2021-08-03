def solve(n, k):
    s = str(n)
    result = ''
    for _ in range(len(s) - k):
        i = min(range(k + 1), key=s.__getitem__)
        result += s[i]
        k -= i
        s = s[i + 1:]
    return result

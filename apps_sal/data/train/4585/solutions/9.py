def find(a, b, n):
    if a == 0 and b == 0:
        return 0
    res = f'{a}{b}'
    while len(res) <= n:
        if '1123581347' in res or '1459' in res:
            break
        total = int(res[-2]) + int(res[-1])
        res += str(total)
    if not ('1123581347' in res or '1459' in res):
        return int(res[n])
    if '1123581347' in res:
        return int('1123581347'[(n - res.index('1123581347')) % 10])
    return int('1459'[(n - res.index('1459')) % 4])

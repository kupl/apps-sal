def max_number(n):
    res = []
    for i in str(n):
        res.append(i)
    res2 = []
    for i in res:
        res2.append(int(i))
    ans = ""
    for i in sorted(res2, reverse=True):
        ans += str(i)
    return int(ans)


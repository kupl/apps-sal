def super_size(n):
    n = list(str(n))
    ans = ''
    while len(n) > 0:
        temp = max(n)
        ans += temp
        n.remove(temp)
    return int(ans)

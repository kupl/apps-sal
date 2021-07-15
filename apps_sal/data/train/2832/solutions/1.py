def array_equalization(a, k):
    keys = set(a)
    ans = []
    for x in keys:
        i = 0
        c = 0
        while i < len(a):
            if a[i] == x:
                i += 1
            else:
                c += 1
                i += k
        ans.append(c)
    return min(ans)

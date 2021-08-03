def zfunc(s):
    if not s:
        return []
    n = len(s)
    Z = [n] * n
    l = r = 0
    for i in range(1, n):
        if i > r:
            l = r = i
            while r < n and s[r - l] == s[r]:
                r += 1
            Z[i] = r - l
            r -= 1
        else:
            k = i - l
            if Z[k] < r - i + 1:
                Z[i] = Z[k]
            else:
                l = i
                while r < n and s[r - l] == s[r]:
                    r += 1
                Z[i] = r - l
                r -= 1
    return Z

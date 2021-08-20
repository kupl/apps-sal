def zfunc(s):
    if s == '':
        return []
    (n, ans) = (len(s), [0] * len(s))
    (ans[0], i, j) = (n, 1, 0)
    while i < n:
        while i + j < n and s[j] == s[i + j]:
            j += 1
        ans[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i + k < n and k + ans[k] < j:
            ans[i + k] = ans[k]
            k += 1
        i += k
        j -= k
    return ans

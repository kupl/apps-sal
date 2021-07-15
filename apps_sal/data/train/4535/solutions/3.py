def zfunc(str_):
    if not str_:
        return []
    n = len(str_)
    z = [0] * n
    left, right, z[0] = 0, 0, n
    for i in range(1, n):
        if i < right:
            k = i - left
            if z[k] < right - i:
                z[i] = z[k]
                continue
            left = i
        else:
            left = right = i
        while right < n and str_[right - left] == str_[right]:
            right += 1
        z[i] = right - left
    return z

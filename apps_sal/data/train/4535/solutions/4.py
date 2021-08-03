def zfunc(s):
    z = [len(s)] + [0] * (len(s) - 1) if s else []
    i, j = 1, 0
    while i < len(s):
        while i + j < len(s) and s[j] == s[i + j]:
            j += 1
        z[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i + k < len(s) and k + z[k] < j:
            z[i + k] = z[k]
            k += 1
        i += k
        j -= k
    return z

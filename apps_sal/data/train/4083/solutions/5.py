def performant_smallest(arr, n):
    c = [0] * 51
    o = [0] * n
    for i in arr:
        c[i] += 1
    (j, st) = (0, len(arr) - n)
    for m in range(50, -1, -1):
        j += c[m]
        if j >= st:
            c[m] = j - st
            break
    j = 0
    for i in arr:
        if i <= m and c[i] > 0:
            o[j] = i
            j += 1
            c[i] -= 1
        if j == n:
            break
    return o

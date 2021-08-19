def hamming(n):
    num = [1]
    (i, j, k) = (0, 0, 0)
    if n == 1:
        return 1
    else:
        for e in range(1, n):
            x = min(2 * num[i], 3 * num[j], 5 * num[k])
            num.append(x)
            if 2 * num[i] <= x:
                i += 1
            if 3 * num[j] <= x:
                j += 1
            if 5 * num[k] <= x:
                k += 1
    return num[len(num) - 1]

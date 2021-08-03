def A(arr, a, b, c, L, T):
    if c < L:
        T.append(arr[a] + arr[b] + arr[c])
    if a == L - 2:
        return 0
    elif b == L - 2:
        return A(arr, a + 1, a + 2, a + 3, L, T)
    elif c == L - 1:
        return A(arr, a, b + 1, b + 2, L, T)

    return A(arr, a, b, c + 1, L, T)


def closest_sum(ints, num):
    print((num, ints))
    T = []
    A(ints, 0, 1, 2, len(ints), T)
    print(T)
    if num in T:
        return num
    else:
        l, h = num, num
        while True:
            l -= 1
            h += 1
            if l in T and h in T:
                return l if T.index(l) < T.index(h) else h
            if l in T:
                return l
            if h in T:
                return h

def n_linear(m, n):
    arr = [1]
    indices = [0] * len(m)
    r = range(len(m))
    count = 0
    while count < n:
        x = min([arr[indices[i]] * m[i] for i in r])
        for i in r:
            if x == arr[indices[i]] * m[i]:
                indices[i] += 1
        arr.append(x + 1)
        count += 1

    return arr[-1]

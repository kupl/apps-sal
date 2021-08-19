def uf_f(arr):
    (a, i) = ([], 0)
    while i < len(arr):
        if isinstance(arr[i], list):
            a.append(uf_f(arr[i]))
            i += 1
        else:
            r = arr[i] % (len(arr) - i)
            if r < 3:
                a.append(arr[i])
                i += 1
            else:
                a.append(arr[i:i + r])
                i += r
    return a


def uf_r(arr):
    (a, i) = ([], len(arr) - 1)
    while i >= 0:
        if isinstance(arr[i], list):
            a.insert(0, uf_r(arr[i]))
            i -= 1
        else:
            r = arr[i] % (i + 1)
            if r < 3:
                a.insert(0, arr[i])
                i -= 1
            else:
                a.insert(0, arr[i - r + 1:i + 1])
                i -= r
    return a


def unflatten(array, depth):
    while depth:
        array = uf_f(array)
        depth -= 1
        if depth:
            array = uf_r(array)
            depth -= 1
    return array

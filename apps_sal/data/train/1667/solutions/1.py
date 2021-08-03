def unflatten(arr, depth, isLeft=1):
    lst, it = [], enumerate(arr if isLeft else reversed(arr))
    for i, x in it:
        if isinstance(x, list):
            lst.append(unflatten(x, 1, isLeft))
            continue

        n = x % (len(arr) - i)
        if n < 3:
            lst.append(x)
        else:
            gna = [x] + [next(it)[1] for _ in range(n - 1)]
            lst.append(gna if isLeft else gna[::-1])

    if not isLeft:
        lst = lst[::-1]

    return lst if depth == 1 else unflatten(lst, depth - 1, isLeft ^ 1)

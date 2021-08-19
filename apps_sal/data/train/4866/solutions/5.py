def split_all_even_numbers(arr, way):
    if way == 0:
        return sum([[[i // 2 - (not i // 2 & 1), i // 2 + (not i // 2 & 1)], [i]][i & 1] for i in arr], [])
    if way == 1:
        return sum([[[1, i - 1], [i]][i & 1] for i in arr], [])
    if way == 2:
        li = []
        for i in arr:
            if not i & 1:
                (a, b) = next(([k, i // k] for k in range(i - 1, 0, -1) if i % k == 0 and k & 1))
                li.extend([a] * b)
            else:
                li.append(i)
        return li
    return sum([[[1] * i, [i]][i & 1] for i in arr], [])

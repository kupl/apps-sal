def pairwise(arr, n):
    lst = [[e, i] for i, e in enumerate(arr)]
    ans, v = [], []
    for i, e in enumerate(arr):
        if i in v:
            continue
        for j, e2 in enumerate(arr[i + 1:]):
            x = i + 1 + j
            if e + e2 == n and x not in v:
                v.append(i)
                v.append(x)
                ans.append((i, x))
                break
    return sum([i[0] + i[1] for i in ans]) if ans != [] else 0

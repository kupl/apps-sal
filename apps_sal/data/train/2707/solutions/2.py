def last_man_standing(n):
    arr = list(range(1, n + 1))
    while len(arr) > 1:
        odd = []
        for (i, j) in enumerate(arr):
            if i % 2 == 0:
                continue
            odd.append(j)
        arr = odd[::-1]
    return arr[0]

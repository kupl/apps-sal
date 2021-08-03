def get_num(arr):
    c, n, r = 1, 1, {}
    arr.sort()
    for a in arr:
        n *= a
        r[a] = r[a] + 1 if a in r else 1
    for a in r:
        c *= r[a] + 1
    return [n, c - 1, arr[0], n // arr[0]]

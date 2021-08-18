def solve(arr):
    alfabetet = 'abcdefghijklmnopqrstuvwxyz'
    res = []
    r = 0

    for char in arr:
        for a, b in zip(char.lower(), alfabetet):
            if a == b:
                r += 1
        res.append(r)
        r = 0
    return res

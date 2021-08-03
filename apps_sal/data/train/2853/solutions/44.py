def solve(arr):
    r = []
    for i in reversed(arr):
        if i not in r:
            r.append(i)

    return r[::-1]

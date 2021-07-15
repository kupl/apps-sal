def solve(arr):
    r = []
    for v in arr[::-1]:
        if not r or r[-1] < v: r.append(v)
    return r[::-1]

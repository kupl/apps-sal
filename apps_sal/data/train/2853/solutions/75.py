def solve(arr):
    out = []
    for x in arr[::-1]:
        if x in out:
            continue
        out.append(x)
    return out[::-1]

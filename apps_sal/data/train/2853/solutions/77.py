def solve(arr):
    temp = arr[::-1]
    out = []
    for i in range(len(temp)):
        if temp[i] in out:
            continue
        out.append(temp[i])
    return out[::-1]

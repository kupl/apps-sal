def solomons_quest(arr):
    d, count, out = {0: 1, 1: 1, 2: -1, 3: -1}, 0, [0, 0]
    for i in arr:
        count += i[0]
        x = (2**count) * d[i[1]] * i[2]
        if i[1] % 2 == 1: out[0] += x
        else: out[1] += x
    return out

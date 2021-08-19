def sort_time(arr):
    arr = sorted(arr, key=lambda x: x[0])
    out = [['', '00:00']]
    while arr:
        i = next((i for (i, t) in enumerate(arr) if t[0] >= out[-1][1]), None)
        out.append(arr.pop(i if i else 0))
    return out[1:]

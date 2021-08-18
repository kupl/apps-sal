def pick_peaks(arr):
    pos, peaks = [], []
    for i in range(len(arr) - 2):
        a, b, c = list(range(i, i + 3))
        if pos and peaks[-1] == arr[b]:
            condition = True
            for i in range(pos[-1], b):
                condition = condition and arr[i] == arr[b]
            if condition is True:
                continue
        while arr[a] == arr[b] and a > 0:
            a -= 1
        while arr[b] == arr[c] and c < len(arr) - 1:
            c += 1
        if arr[a] < arr[b] and arr[b] > arr[c]:
            pos += [b]
            peaks += [arr[b]]
    return {"pos": pos, "peaks": peaks}

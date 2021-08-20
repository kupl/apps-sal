def interleave(*args):
    max_len = max(map(len, args))
    interleaved = []
    for i in range(max_len):
        for arr in args:
            if i < len(arr):
                interleaved.append(arr[i])
            else:
                interleaved.append(None)
    return interleaved

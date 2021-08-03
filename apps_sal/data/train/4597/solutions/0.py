def combine(*args):
    out = list()
    for i in range(len(max(args, key=len))):  # Sometimes you just have to love python
        for arr in args:
            if i < len(arr):
                out.append(arr[i])
    return out

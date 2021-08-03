def transpose_two_strings(arr):
    mw = max([len(x) for x in arr])
    return "\n".join([" ".join([a, b]) for a, b in zip(arr[0].ljust(mw), arr[1].ljust(mw))])

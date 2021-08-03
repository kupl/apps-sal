def sort_two_arrays(*args):
    sortedIdxRev = [sorted((v, i) for i, v in enumerate(a)) for a in args[::-1]]
    return [[arr[i] for _, i in idx] for arr, idx in zip(args, sortedIdxRev)]

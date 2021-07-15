def series_slices(s, n):
    if n > len(s):
        raise
    
    arr = [int(d) for d in s]
    return [ arr[i:i+n] for i in range(len(s)-n +1) ]

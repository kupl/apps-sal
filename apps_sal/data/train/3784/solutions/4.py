def sort_transform(arr):
    arr  = list(map(chr, arr))
    srtd = sorted(arr)
    
    a = "".join(arr[:2] + arr[-2:])
    b = "".join(srtd[:2] + srtd[-2:])
    
    return f"{a}-{b}-{b[::-1]}-{b}"

def wave_sort(a):
    a.sort()
    size,half = len(a), len(a)>>1
    for low,high in enumerate(range(0,size,2), half):
        a[low],a[high] = a[high],a[low]
    return a

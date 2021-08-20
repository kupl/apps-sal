def wave_sort(a):
    a.sort()
    last = len(a) - len(a) % 2
    (a[1::2], a[:last:2]) = (a[:last:2], a[1::2])

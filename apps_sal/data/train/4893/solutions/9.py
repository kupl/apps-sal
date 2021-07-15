def wave_sort(a):
    s = a[:]
    f = [max, min]
    for i in range(len(a)):
        v = f[i%2](s)
        a[i] = v
        s.remove(v)


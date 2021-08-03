def wave_sort(a):
    a.sort()
    [a.insert(i + 1, a.pop(i)) for i in range(len(a)) if i % 2 == 0]
    return

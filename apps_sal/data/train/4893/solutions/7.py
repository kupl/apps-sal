def wave_sort(a):
    a1, a2 = sorted(a), sorted(a)[::-1]

    for i in range(len(a)):
        if i % 2 == 1:
            a[i] = a1.pop(0)
        else:
            a[i] = a2.pop(0)
    print(a)
    return a

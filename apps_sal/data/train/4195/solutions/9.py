def merge(a):
    a = [i for i in a if i] + [i for i in a if not i]
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            a[i], a[i + 1] = 2 * a[i], 0

    return [i for i in a if i] + [i for i in a if not i]

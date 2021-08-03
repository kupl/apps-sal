def first_tooth(array):
    a = [array[0]] + array + [array[-1]]
    b = [2 * a[i] - a[i - 1] - a[i + 1] for i in range(1, len(a) - 1)]
    c = max(b)
    return b.index(c) if b.count(c) == 1 else -1

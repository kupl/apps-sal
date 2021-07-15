def two_sort(array):
    x = sorted(array)[0]
    s = x[0]
    for l in range(len(x) - 1) :
        s = s + "***" + x[l + 1]
    return s

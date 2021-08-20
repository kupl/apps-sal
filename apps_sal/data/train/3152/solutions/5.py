def interpreter(t, array):
    ls = list(array)
    l = len(t)
    (i, j) = (0, 0)
    while j < len(array):
        if t[i % l] == '1':
            ls[j] = '0' if ls[j] == '1' else '1'
        else:
            j += 1
        i += 1
    return ''.join(ls)

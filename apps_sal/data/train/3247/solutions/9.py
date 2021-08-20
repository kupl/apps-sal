def sort_by_height(a):
    (h, k) = (sorted([i for i in a if i != -1]), [])
    for i in a:
        if i != -1:
            k += [h[0]]
            h = h[1:]
        else:
            k += [i]
    return k

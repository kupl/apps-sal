from random import choice


def nth_smallest(arr, pos):
    ar = list(arr)
    while True:
        if len(ar) == 1:
            return ar[0]
        (big, lit, pivot) = ([], [], choice(ar))
        for i in ar:
            if i > pivot:
                big.append(i)
            elif i < pivot:
                lit.append(i)
        k = len(ar) - len(big)
        if pos > k:
            (ar, pos) = (big, pos - k)
        elif pos > len(lit):
            return pivot
        else:
            ar = lit

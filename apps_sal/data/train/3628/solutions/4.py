def rotate(lst, n):
    n %= len(lst)
    return lst[-n:] + lst[:-n]

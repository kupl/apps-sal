def arr(n=None):
    lst = []
    if n is None:
        return lst
    else:
        while n > 0:
            lst.append(n - 1)
            n -= 1
        return sorted(lst)

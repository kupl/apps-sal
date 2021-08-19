

def arr(n=None):
    # [ the numbers 0 to N-1 ]
    lst = []
    if n is None:
        return lst
    else:
        while n > 0:
            lst.append(n - 1)
            n -= 1
        return sorted(lst)

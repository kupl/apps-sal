def super_size(n):
    lst = list(str(n))
    lst.sort()
    return int(''.join(lst[::-1]))

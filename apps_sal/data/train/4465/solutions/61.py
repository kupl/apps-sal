def super_size(n):
    lst = [i for i in str(n)]
    return int(''.join(sorted(lst, reverse=True)))

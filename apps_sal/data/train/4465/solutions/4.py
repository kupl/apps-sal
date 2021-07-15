def super_size(n):
    list_ = sorted(list(str(n)))
    list_.reverse()
    return int(''.join(tuple(list_)))

def super_size(n):
    li = list(str(n))
    li.sort(reverse = True)
    return int(''.join(li))

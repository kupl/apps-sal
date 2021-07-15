def replace_zero(arr):
    m, im, i, lst = 0, -1, -1, ''.join(map(str,arr)).split('0')
    for a,b in zip(lst,lst[1:]):
        i += len(a) + 1 
        candidate = len(a)+len(b)+1
        if m <= candidate:
            im, m = i, candidate
    return im

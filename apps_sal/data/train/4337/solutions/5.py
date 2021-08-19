def swap_head_tail(a):
    return a[len(a) + 1 >> 1:] + a[len(a) >> 1:len(a) + 1 >> 1] + a[:len(a) >> 1]

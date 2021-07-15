def swap_head_tail(a):
    r, l = (len(a)+1)//2, len(a)//2
    return a[r:] + a[l:r] +  a[:l]

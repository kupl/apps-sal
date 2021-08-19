def swap_head_tail(a):
    return (lambda m: a[-m:] + a[m:-m] + a[:m])(len(a) // 2)

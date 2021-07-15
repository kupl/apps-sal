swap_head_tail = lambda a: a[len(a)+1>>1:] + a[len(a)>>1:len(a)+1>>1] + a[:len(a)>>1]

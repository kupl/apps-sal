def split_and_add(a, n):    
    return split_and_add([sum(e) for e in zip(([0] if len(a) % 2 else []) + a[:len(a)//2], a[len(a)//2:])], n - 1) if n else a

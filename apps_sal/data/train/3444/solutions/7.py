def cyclic_string(s):
    l=len(s)
    return next(i for i in range(1,l+1) if s==(s[:i]*l)[:l])

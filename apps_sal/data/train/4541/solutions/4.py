def array_operations(a, k):
    b = [max(a)-i for i in a]
    c = [max(b)-i for i in b]
    return b if k%2 else c if k>0 else a

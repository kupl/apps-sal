def find_spec_partition(n, k, com):
    x,r = divmod(n,k)
    return {'max': [x+1]*r + [x]*(k-r),
            'min': [n+1-k] + [1]*(k-1)}[com]

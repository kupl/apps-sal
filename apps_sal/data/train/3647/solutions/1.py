def solve(arr):
    lmax, lmin = iter(sorted(arr)) , iter(sorted(arr)[::-1])
    return [next(lmax) if i%2==1 else next(lmin) for i in range(0,len(arr))]

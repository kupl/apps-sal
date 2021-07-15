def n_closestPairs_tonum(n, k):
    a = [i**2 for i in range(1, int((2*n)**0.5)+1)]
    res = [[(s1+s2)/2, (s2-s1)/2] for i, s1 in enumerate(a) for s2 in a[i+1:] if s1+s2<2*n and (s1+s2)%2==0]
    return sorted(res, key=lambda sl: (-sl[0], -sl[1]))[:k]

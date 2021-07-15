def n_closestPairs_tonum(num, k):
    #m+n=p**2
    #m-n=q**2 => n=m-q**2
    result = []
    for m in range(num-1,1,-1):
        for q in range(1,int(m**.5)):
            n=m-q**2
            if int((m+n)**.5)**2 == m+n:
                result.append([m, n])
                if len(result)==k:
                    return result
    return result

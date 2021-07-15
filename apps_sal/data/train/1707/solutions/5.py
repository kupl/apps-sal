def cut_log(p, n):
    # store the optimal prices of logs 
    plogs = [0]*len(p)
    for j in range(1, n+1):
        val = p[j]
        # second loop actually only has to iterate over a set half
        # the length of the current log since you're adding values
        # from either end.
        for i in range(1, j//2+1):
            # compare prices using optimal prices for lengths
            # smaller than your current length target, take max
            sm = plogs[i] + plogs[j-i]
            if sm > val:
                val = sm
        plogs[j] = val
    return plogs[n]

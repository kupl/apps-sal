def n_closestPairs_tonum(num, k):
    r=[]
    m=2
    while(m*m<num):
        for n in range(1,m):
            if (m*m+n*n>=num):
                break
            r.append([m*m+n*n,2*m*n])
        m+=1
    return sorted(r,reverse=True)[:k]

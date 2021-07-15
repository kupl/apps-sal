def n_linear(m,n):
    arr = [1]
    ms = list(m)
    idxs = [0] * len(ms)
    r = range(len(ms))
    
    for i in range(n):
        vals = [arr[idxs[j]]*ms[j]+1 for j in r]
        val = min(vals)
        arr.append(val)
        
        for j in r:
            idxs[j] += 1*(val==vals[j])
            
    return arr[n]

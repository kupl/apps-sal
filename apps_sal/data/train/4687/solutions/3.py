def decomp(n):
    f = {}
    for  i in range(2, n+1):
        for j in range(2, int(i**0.5)+1):
            while i%j==0:
                i = i//j
                if j in f: f[j] += 1
                else: f[j] = 1
        if i!=1:
            if i in f: f[i] += 1
            else: f[i] = 1
        
    return ' * '.join(["{}^{}".format(i, f[i]) if f[i]>1 else str(i) for i in sorted(f)])

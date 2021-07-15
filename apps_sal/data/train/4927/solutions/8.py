from functools import reduce
from itertools import accumulate
def transform(a,x):
    b=sorted(set([x]+a))
    C=[[1]]
    def g(m,n):
        w=[C[-1][-1]]
        for i,j in enumerate(m,start=1):
            w.append(w[i-1]*j/(j-n))
        return C.append(w[1:])
    for j in (range(b[i-1]+1,b[i]+1) for i in range(1,len(b))):
        g(j,x)
    v={x:y for x,y in zip(b,accumulate(int(sum(i)) for i in C))}
    return reduce(lambda x,y:x^y,[v[i] for i in a])

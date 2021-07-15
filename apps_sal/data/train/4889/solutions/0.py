from itertools import cycle,chain

def max_hexagon_beam(n,seq):
    h    = 2*n-1
    seq  = cycle(seq)
    sums = [ [0]*h for _ in range(3)]            # [horz, diagUp, diagDown]
    
    for r in range(h):
        for c,v in zip(list(range(n+r if r<n else h+n-1-r)),seq):
            idxs = (r, c+max(0,r-n+1), c+max(0,n-1-r))
            for i,j in enumerate(idxs): sums[i][j] += v
            
    return max(chain.from_iterable(sums))


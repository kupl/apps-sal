# cook your dish here
import math
read = lambda : list(map(int,input().strip().split()))
rs = lambda :  int(input().strip())
t = rs()
ans = []
find_edges = lambda n,k : min(max_edges(n,k),k)
max_edges = lambda n,k : ((n-k+1) * (n-k)) >> 1
def find(n):
    # x = (n * (n+1));
    # other  = (2*n) + 3;
    l = (n >> 1) + (n%2); 
    r = n;
    while l + 1 < r:
        mid = l  + ((r-l) >> 1);
        if max_edges(n,mid) < mid:
            r = mid - 1;
        else:
            l = mid;
    if max_edges(n,r) >= r:
        return find_edges(n,r);
    else:
        return find_edges(n,l);
        

    
for _ in range(t):
    n = rs()
    ans.append(find(n))
print("\n".join([str(x) for x in ans]))

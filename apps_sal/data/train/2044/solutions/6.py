def pr(m):
    for i in range(len(m)):
        print(' '.join([str(x) for x in m[i]]))

n, k = map(int, input().split())
edge = [[1, v] if v < k+1 else [v-k, v] for v in range(2, n+1)]

def get_min_max_radius(n, k):
    r    = (n-1) % k
    base = (n-1) // k
    
    if r == 0:
        return base * 2
    
    if r == 1:
        return base * 2 + 1
    
    return base * 2 + 2    
    
print(get_min_max_radius(n, k))    
pr(edge)

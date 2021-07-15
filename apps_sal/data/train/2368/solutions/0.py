t = int(input())

for _ in range(t):
    n = int(input())
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ma = min(a)
    mb = min(b)
    
    ops = 0
    for xa, xb in zip(a, b):
        da = xa - ma
        db = xb - mb
        ops += max(da, db)
        
    print(ops)


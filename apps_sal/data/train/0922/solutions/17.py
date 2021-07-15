t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    sa = set(a)
    
    sb = set(b)
    
    ans = set()
    
    for i in sa:
        if i not in sb:
            ans.add(i)
    
    for i in sb:
        if i not in sa:
            ans.add(i)
    
    print(*sorted(ans))

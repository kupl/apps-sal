for _ in range(int(input())):
    x,y = list(map(int,input().split()))
    a = max(x,y)
    b = min(x,y)
    while a%b!=0:
        a = a%b
        p = a
        q = b
        a = max(p,q)
        b = min(p,q)
        
    if a==1 or b==1:
        print('YES')
    else:
        print('NO')


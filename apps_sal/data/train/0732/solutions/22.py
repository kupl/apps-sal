t = int(input())
while(t > 0):
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s = 0
    da, db = 0, 0
    for i in range(n):
        da += a[i]
        db += b[i]
        if(a[i] == b[i] and da == db):
            s += a[i]
    print(s)

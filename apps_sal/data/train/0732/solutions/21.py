# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    p = q = d = 0
    for i in range(n):
        p += a[i]
        q += b[i]
        if(p == q and a[i] == b[i]):
            d += a[i]
            # print(d)
    print(d)

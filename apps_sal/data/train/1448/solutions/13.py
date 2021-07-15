for _ in range(int(input())):
    a,d,k,n,inc = map(int,input().split())
    ans = a
    for i in range(1,n):
        if i % k == 0:
            d += inc
            ans += d
        else:
            ans += d
    print(ans)

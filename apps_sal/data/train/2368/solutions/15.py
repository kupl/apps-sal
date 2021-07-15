for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ma = min(a)
    mb = min(b)
    ans = 0
    for i in range(0,n):
        ta = a[i]-ma
        tb = b[i]-mb
        ans += max(ta,tb)
    print(ans)


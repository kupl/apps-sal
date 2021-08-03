# cook your dish here
t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))
    m = list(map(int, input().split()))
    d = m[0] - l[0]
    e = m[1] - l[1]
    f = m[2] - l[2]
    if(d < 0 or e < 0 or f < 0):
        print(-1)
    else:
        ans = 0
        if(d > 0):
            ans += d
        if(e > 0):
            ans += e
        if(f > 0):
            ans += f
        print(ans)

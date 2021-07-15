Q = int(input())
for i in range(Q):
    a,b = map(int,input().split())
    if a > b: a,b = b,a
    if b in (a, a+1):
        print((a-1)*2)
        continue
    c = int((a*b)**0.5)
    if c*c == a*b:
        c -= 1
    ans = 2*c - 2
    if c*(c+1) < a*b:
        ans += 1
    print(ans)

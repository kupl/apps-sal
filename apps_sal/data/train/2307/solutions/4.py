n, a, b = list(map(int, input().split()))
xlist = list(map(int, input().split()))

ans = 0
for i in range(n-1):
    ans += min((xlist[i+1]-xlist[i])*a, b)

print(ans)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    c = []
    a.sort()
    for i in range(n-1):
        c.append(a[i+1]-a[i])
    print(min(c))

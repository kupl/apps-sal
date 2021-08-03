t = int(input())
while t:
    t -= 1
    n = int(input())
    lst = list(map(int, input().split()))
    new = []
    su = 0
    for i in range(n):
        su = su + lst[i]
        new.append(su)
    i = 0
    ans = 0
    while(i < n - 1):
        i = i + new[i]
        ans += 1
    print(ans)

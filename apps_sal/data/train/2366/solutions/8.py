t = int(input())
while t:
    n = int(input())
    a = list(map(int, input().split()))
    a.reverse()
    minn = a[0]
    ans = 0
    for i in range(1, n):
        if a[i] > minn:
            ans += 1
        minn = min(minn, a[i])
    print(ans)
    t -= 1

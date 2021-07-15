for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = [-1]*n
    b[n-1] = a[n-1]
    ans = 0
    for i in range(n-2, -1, -1):
        b[i] = min(b[i+1], a[i])
    for i in range(n-1):
        if(a[i] > b[i]):
            ans += 1
    print(ans)


for _ in range(int(input())):
    n, d = list(map(int, input().split()))
    ar = list(map(int, input().split()))
    ans = ar[0]
    for i in range(1, n):
        if ar[i] * i <= d:
            d -= ar[i] * i
            ans += ar[i]
        else:
            ans += d // i
            break
    print(ans)

for t in range(int(input())):
    (n, k) = map(int, input().split())
    ans = 2 * n - 2 * ((n - 1) / k)
    print(ans)

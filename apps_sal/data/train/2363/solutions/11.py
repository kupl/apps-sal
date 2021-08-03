for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    ar.sort()
    ans = 10000000000
    for i in range(1, n):
        ans = min(abs(ar[i] - ar[i - 1]), ans)
    print(ans)

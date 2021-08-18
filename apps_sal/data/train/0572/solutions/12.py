for i in range(int(input())):
    n, m, k = map(int, input().split())
    if abs(n - m) <= k:
        print(0)
    else:
        print(abs(n - m) - k)

for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    print(k * ((n + 1) // 2))

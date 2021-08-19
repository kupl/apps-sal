for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    if n % 2 == 0:
        print(k * (n // 2))
    else:
        print(k * (n // 2 + 1))

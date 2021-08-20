for _ in range(int(input())):
    (a, b, c) = sorted(map(int, input().split()))
    ans = a * (b - 1) * (c - 2)
    print(ans % (10 ** 9 + 7) if ans > 0 else 0)

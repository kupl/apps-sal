try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        gcd = max(a[0], a[-1])

        print(gcd)
except EOFError:
    pass

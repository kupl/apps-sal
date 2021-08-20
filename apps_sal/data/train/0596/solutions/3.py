try:
    t = int(input())
    for _ in range(t):
        (a, b) = map(int, input().split())
        if a == 0:
            print((b - 1) * b % 1000000007)
        else:
            c = b % 2
            if c == 0:
                x = (b - 2) // 2
                ans = (a + x) * (a + x + 1) + a
                print(ans % 1000000007)
            else:
                x = b // 2
                ans = (a + x - 1) * (a + x)
                ans = ans + a + 2 * x
                print(ans % 1000000007)
except:
    pass

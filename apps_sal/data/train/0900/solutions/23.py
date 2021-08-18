

def __starting_point():
    tc = int(input().strip())

    for t in range(tc):
        k = int(input().strip())

        ans = 10
        mod = int(1e9 + 7)
        for i in range(1, k):
            ans = (2 * (ans % mod)) % mod

        print(ans)


__starting_point()

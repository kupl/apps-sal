def __starting_point():
    tests = int(input())
    for _ in range(tests):
        n, b, m = list(map(int, input().split()))
        ans = 0
        itr = 1
        k = n
        k1 = n
        while(k >= 1):
            if k % 2 == 0:
                k = k // 2
            else:
                k = (k + 1) // 2
            ans += k * (itr * m)
            k = k1 - k
            k1 = k
            ans += b
            itr *= 2

        print(ans - b)


__starting_point()

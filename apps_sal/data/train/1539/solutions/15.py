def __starting_point():
    t = int(input().strip())
    for test in range(t):
        s1 = input().strip()
        d1 = {}
        for i in s1:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        s2 = input().strip()
        ans = 0
        for i in s2:
            if i in d1:
                d1[i] -= 1
                ans += 1
        print(ans)


__starting_point()

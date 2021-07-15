def __starting_point():

    for _ in range(int(input())):
        res = 0
        n = int(input())
        m = []
        for i in range(n):
            m.append(list(map(int, input().split())))
        zeroes = 0
        for a in m:
            for el in a:
                if el == 0:
                    zeroes = zeroes + 1
        for i in range(n):
            if i < n-1:
                x = i * 2 + 2
            else:
                x = n
            if x > zeroes:
                res = i
                break
            elif x == zeroes:
                res = i + 1
                break
            else:
                zeroes = zeroes - x
        if res == n:
            res = res - 1
        print(n-1-res)


__starting_point()

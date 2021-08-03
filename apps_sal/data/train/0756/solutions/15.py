try:
    t = int(input())
    for i in range(t):
        a, b = map(int, input().split())
        c = a + b
        c1 = c + 1
        while c1 != 0:
            for j in range(2, c1):
                if (c1 % j) == 0:
                    c1 += 1
                    break
            else:
                c2 = c1
                c1 = 0
                break
        print(c2 - c)
except:
    pass

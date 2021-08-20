try:
    t = int(input())
    for _ in range(t):
        p = list(map(int, input().split()))
        (x, k) = (p[0], p[1])
        (c1, c2) = (0, 0)
        for i in range(2, x + 1):
            if x % i == 0:
                c1 += pow(i, k)
        for i in range(2, k + 1):
            if k % i == 0:
                c2 += x * i
        print(c1, c2)
except:
    pass

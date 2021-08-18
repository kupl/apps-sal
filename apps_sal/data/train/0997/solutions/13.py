try:
    for _ in range(int(input())):
        n, m = map(int, input().split())
        l = [10] * n
        for i in range(m):
            s, e, v = map(int, input().split())
            for i in range(s - 1, e):
                l[i] *= v
        print(sum(l) // n)

except:
    pass

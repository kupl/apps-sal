for _ in range(int(input())):
    n, m = sorted(list(map(int, input().split())))
    if(2 * n < m):
        print(m * m)
    else:
        print((2 * n)**2)

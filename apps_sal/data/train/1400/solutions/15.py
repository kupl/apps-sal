for _ in range(int(input())):
    mini, maxi = 0, 0
    n, l, r = map(int, input().split())
    o = n - l + 1
    t = n - r + 1
    for i in range(1, n - o + 1):
        mini = mini + 2**i
    maxi = maxi + t * (2**(r - 1))
    for j in range(r - 2, r - 2 - (n - t), -1):
        maxi = maxi + 2**j
    print(mini + o, maxi)

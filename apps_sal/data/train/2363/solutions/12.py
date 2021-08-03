for i in range(int(input())):
    c = int(input())
    f = sorted([int(i) for i in input().split()])
    k = 1000000000000
    for j in range(1, c):
        k = min(k, f[j] - f[j - 1])

    print(k)

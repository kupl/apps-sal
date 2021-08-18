for _ in range(int(input())):
    n, x, m = list(map(int, input().split()))
    l = list(map(int, input().split()))
    q = []
    for j in range(m):
        for i in range(1, len(l)):
            l[i] = l[i] + l[i - 1]
    print(l[x - 1] % (10**9 + 7))

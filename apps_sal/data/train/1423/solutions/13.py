try:
    lt = []
    for _ in range(int(input())):
        N = int(input())
        N_lt = list(map(int, input().split()))
        K = N_lt[int(input()) - 1]
        N_lt = sorted(N_lt)
        lt.append(N_lt.index(K))
    for i in lt:
        print(i + 1)
except:
    pass

import random 
for _ in range(int(input())):
    N, M = list(map(int, input().split()))
    X = [[int(a) for a in input().split()] for _ in range(N)]
    Y = [[X[i][j] for i in range(N)] for j in range(M)]
    ma = 0
    for t in range(99):
        for i in range(M):
            a = random.randrange(N)
            Y[i] = [Y[i][j-a] for j in range(N)]
        ma = max(ma, sum([max([Y[i][j] for i in range(M)]) for j in range(N)]))
    print(ma)


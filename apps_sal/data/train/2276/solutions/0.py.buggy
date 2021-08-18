rnd_mod = 1234567890133
rnd_x = 987654321098


def rnd():
    nonlocal rnd_x
    rnd_x = rnd_x**2 % rnd_mod
    return (rnd_x >> 5) % (1 << 20)


def randrange(a):
    return rnd() % a


T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split()))
    X = []
    for __ in range(N):
        X.append([int(a) for a in input().split()])
    Y = [[X[i][j] for i in range(N)] for j in range(M)]
    ma = 0
    for t in range(577):
        for i in range(M):
            a = randrange(N)
            Y[i] = [Y[i][j - a] for j in range(N)]
        ma = max(ma, sum([max([Y[i][j] for i in range(M)]) for j in range(N)]))
    print(ma)

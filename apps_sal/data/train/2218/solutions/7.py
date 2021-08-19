import sys
sys.setrecursionlimit(10 ** 5 + 1)
inf = int(10 ** 20)
max_val = inf
min_val = -inf


def RW():
    return sys.stdin.readline().strip()


def RI():
    return int(RW())


def RMI():
    return [int(x) for x in sys.stdin.readline().strip().split()]


def RWI():
    return [x for x in sys.stdin.readline().strip().split()]


nb = RI()
have = RMI()
nb_ops = RI()
curr = [-1] * nb
maxs = 0
ops = [RMI() for _ in range(nb_ops)][::-1]
for i in ops:
    if i[0] == 2:
        maxs = max(maxs, i[1])
    elif curr[i[1] - 1] == -1:
        curr[i[1] - 1] = max(maxs, i[2])
for i in range(nb):
    if curr[i] == -1:
        curr[i] = max(maxs, have[i])
print(*curr)

from sys import stdin
rl = stdin.readline


def read(func=int):
    return map(func, rl().strip().split())


for _ in range(int(rl())):
    n = int(rl())

    profit = []
    for _ in range(n):
        s, p, v = read()
        if s < p:
            profit.append(((p) // (s + 1)) * v)

    print(max(profit)) if len(profit) > 1 else print(0)

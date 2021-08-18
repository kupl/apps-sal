import math
t = int(input())


def do():
    n, k, v = list(map(int, input().split()))
    a = [int(d) for d in input().split()]
    r = 0
    r = ((v * (n + k) - sum(a)) // k)
    if r <= 0:
        print(-1)
    elif((v * (n + k) - sum(a)) % k != 0):
        print(-1)
    else:
        print(r)
    return


for i in range(t):
    do()

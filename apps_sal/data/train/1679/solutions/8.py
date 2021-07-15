from math import ceil

for T in range(int(input())):
    N, K, X = map(int, input().split())
    print(' '.join(map(str, (([X] + [0] * (K - 1)) * ceil(N/K))[:N])))

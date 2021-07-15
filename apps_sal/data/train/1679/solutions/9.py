from math import ceil

def raavan(N, K, X):
    return ' '.join(map(str, (([X] + [0] * (K - 1)) * ceil(N/K))[:N]))

for T in range(int(input())):
    N, K, X = map(int, input().split())
    print(raavan(N, K, X))

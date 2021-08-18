import math


def poisson_p(k, P):
    result = 1
    for i in range(1, k + 1):
        result *= P / i

    return result * math.exp(-P)


V = int(input())

for _ in range(V):
    ks = list(map(int, input().split()))
    N = len(ks)
    P = sum(ks) / N
    var = sum((k - P)**2 for k in ks) / N
    poisson_var = P
    uniform_var = 2 / (2 * P + 1) * sum(a**2 for a in range(round(P) + 1))
    print(('poisson' if abs(var - poisson_var) < abs(var - uniform_var)
          else 'uniform'))

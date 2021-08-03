# this is [A000110, A002870, A024417]

# Stirling numbers of second kind
# http://mathworld.wolfram.com/StirlingNumberoftheSecondKind.html
# S(n,k) = S(n-1,k-1)+k*S(n-1,k)
S = {}
for n in range(1, 1800):
    S[(n, 1)] = S[(n, n)] = 1
    for k in range(2, n):
        S[(n, k)] = S[(n - 1, k - 1)] + k * S[(n - 1, k)]


def combs_non_empty_boxesII(n):
    ss = [(S[(n, k)], k) for k in range(1, n + 1)]
    return [sum(p[0] for p in ss), *max(ss)]

from functools import reduce
def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
T = int(input())
while T:
    X, K = input().split()
    X, K = int(X), int(K)
    factors_X = factors(X)
    factors_K = factors(K)
    factors_X.remove(1)
    factors_K.remove(1)
    sum_X = 0
    sum_K = 0
    for i in factors_X:
        sum_X += (i ** K)
    for i in factors_K:
        sum_K += (i * X)
    print(sum_X, sum_K)
    T -= 1

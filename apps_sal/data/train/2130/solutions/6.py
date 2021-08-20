import math


def read_data():
    k = int(input())
    ns = [int(input()) for i in range(k)]
    return (k, ns)


def solve(k, ns):
    n = sum(ns)
    free_pos = n
    result = 1
    mod = 10 ** 9 + 7
    for ni in reversed(ns):
        tmp = math.factorial(free_pos - 1) // math.factorial(free_pos - ni)
        tmp //= math.factorial(ni - 1)
        tmp %= mod
        result *= tmp
        result %= mod
        free_pos -= ni
    return result


(k, ns) = read_data()
print(solve(k, ns))

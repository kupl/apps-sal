def S(n):
    return n * (n + 1) // 2


def result(a, b):
    return S(b - 1) * b * S(a) + S(b - 1) * a


a, b = list(map(int, input().split()))
mod = 10**9 + 7
print(result(a, b) % mod)

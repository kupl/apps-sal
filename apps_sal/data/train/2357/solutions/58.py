(N, M) = list(map(int, input().split()))
A = [int(i) for i in input().split()]
sumA = sum(A)
mod = 10 ** 9 + 7


def inv(x):
    return pow(x, mod - 2, mod)


ans = 1
F = 1
for i in range(N + sumA):
    ans *= N + M - i
    ans %= mod
    F *= i + 1
    F %= mod
ans *= inv(F)
ans %= mod
print(ans)

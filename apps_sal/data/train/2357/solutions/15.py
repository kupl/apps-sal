(N, M) = map(int, input().split())
A = list(map(int, input().split()))
mod = 10 ** 9 + 7
invs = [0, 1]
X = N + M
Y = N + sum(A)


def inv(x):
    if x == 1:
        return 1
    else:
        return -invs[mod % x] * (mod // x) % mod


for i in range(2, Y + 1):
    invs.append(inv(i))
ans = 1
for i in range(Y):
    ans *= (X - i) * invs[i + 1]
    ans %= mod
print(ans % mod)

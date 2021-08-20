(N, M) = list(map(int, input().split()))
A = list(map(int, input().split()))
S = sum(A)
MOD = 10 ** 9 + 7
a = b = 1
for i in range(1, S + N + 1):
    a *= M + N + 1 - i
    a %= MOD
    b *= i
    b %= MOD
ans = a * pow(b, MOD - 2, MOD)
ans %= MOD
print(ans)

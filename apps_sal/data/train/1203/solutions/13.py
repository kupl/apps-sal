z = (10**9 + 7)

fact = []
fact.append(1)
for i in range(1, 4000):
    fact.append(i * fact[i - 1] % z)


def factorialMod(n):
    ans = 1
    for i in range(1, n + 1):
        ans = ans * i % z
    return ans % z


def nCr(n, r):
    if r > n:
        return 0
    return fact[n] * pow(fact[r] * fact[n - r], z - 2, z) % z


for _ in range(0, int(input())):
    n, q = list(map(int, input().split()))
    for __ in range(0, q):
        i, k = list(map(int, input().split()))
        a = nCr(i - 1, k - 1)
        b = pow(2, n - i, z)
        print((a * b) % z)

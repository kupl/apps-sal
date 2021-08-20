MOD = 10 ** 9 + 7


def power(a, n):
    ans = 1
    while n:
        if n & 1:
            ans = ans * a % MOD
        a = a * a % MOD
        n >>= 1
    return ans


fact = [1] * 200013
for i in range(1, 200013):
    fact[i] = fact[i - 1] * i % MOD
inv = [1] * 200013
for i in range(2, 200013):
    inv[i] = power(fact[i], MOD - 2)


def C(n, k):
    return fact[n] * inv[k] * inv[n - k] % MOD


(h, w, n) = map(int, input().split(' '))
mas = []
for i in range(n):
    (x, y) = map(int, input().split(' '))
    mas.append([x, y, 0, 0])
mas.append([h, w, 0, 0])
mas.sort(key=lambda x: x[0] + x[1])
for j in mas:
    j[2] = C(j[0] + j[1] - 2, j[0] - 1) % MOD
    for i in mas:
        if j[0] == i[0] and j[1] == i[1]:
            break
        if i[0] <= j[0] and i[1] <= j[1]:
            l = C(j[0] - i[0] + j[1] - i[1], j[0] - i[0]) % MOD
            k = i[2]
            j[2] -= l * k % MOD
print(mas[-1][2] % (10 ** 9 + 7))

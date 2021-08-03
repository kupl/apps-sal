kk = 1
f = [0] * 1001
f[0] = 1
for i in range(1, 1001):
    kk *= i
    kk %= (10**9 + 7)
    f[i] = pow(kk, 10**9 + 5, 10**9 + 7)


def c(n, k):
    prod = 1
    for i in range(n - k + 1, n + 1):
        prod *= i
        prod %= (10**9 + 7)
    prod = (prod * f[k]) % (10**9 + 7)

    return prod


l = []
m = []
a = 1
s = 0
for i in range(int(input())):
    x = int(input())
    s += x
    l.append(s - 1)
    m.append(x - 1)

ans = 1
for i in range(len(l)):
    ans = (ans * c(l[i], m[i])) % (10**9 + 7)
print(ans)

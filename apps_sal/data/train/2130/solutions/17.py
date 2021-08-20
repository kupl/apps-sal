k = int(input())
a = []
for _ in range(k):
    a.append(int(input()))
n = sum(a)
N = 1000000007


def getCombi(a, n):
    b = min(a, n - a)
    ret = 1
    for i in range(1, b + 1):
        ret = ret * (n + 1 - i) // i
    return ret % N


ret = 1
for i in range(k - 1, 0, -1):
    ai = a[i] - 1
    ni = sum(a[:i])
    ret *= getCombi(ai, ni + ai)
    ret %= N
print(ret)

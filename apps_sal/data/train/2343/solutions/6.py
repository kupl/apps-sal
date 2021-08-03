def calc(n):
    a = n.bit_length() - 1
    X = [0] * 30
    X[a] = n - (1 << a) + 1
    for i in range(a):
        X[i] = 1 << i
    return X


T = int(input())
for _ in range(T):
    d, m = list(map(int, input().split()))
    s = 1
    for a in calc(d):
        s = s * (a + 1) % m
    print((s - 1) % m)

(a, b) = ([0] * 101001, [0] * 101001)
mod = pow(10, 9) + 7
a[0] = 1
b[0] = 0
a[1] = 0
b[1] = 1
b[2] = b[1] + b[0] + b[0]
a[2] = a[1] + a[0] + a[0]
for u in range(3, 100001):
    b[u] += (b[u - 1] + b[u - 2] + b[u - 3]) % mod
    a[u] += (a[u - 1] + a[u - 2] + a[u - 3]) % mod
for t in range(eval(input())):
    x = eval(input())
    print(a[x], b[x])

from math import ceil
t = int(input())
for i in range(t):
    n = int(input())
    m = 10 ** 9 + 7
    z = 26 * (pow(26, ceil(n / 2), m) % m - 1) * 280000002
    if n % 2 == 0:
        z *= 2
    else:
        c = n - 1
        f = 26 * (pow(26, ceil(c / 2), m) % m - 1 % m) * 280000002
        z += f
    print(z % m)

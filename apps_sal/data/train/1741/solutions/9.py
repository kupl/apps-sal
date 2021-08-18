N, m, five_by_2n = 12345787, {0: 1, 1: 8, 2: 95, 3: 1183}, lambda n: m[n]
for n in range(4, 10001):
    m[n] = (15 * m[n - 1] - 32 * m[n - 2] + 15 * m[n - 3] - m[n - 4]) % N

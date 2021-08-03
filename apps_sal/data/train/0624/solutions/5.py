z, a, b = (10**9 + 7), [0] * 100007, [0] * 100007
b[0], b[1], a[2] = 1, 1, 1
for i in range(3, 100007):
    a[i] = a[i - 1] + a[i - 2] + a[i - 3]
    b[i] = b[i - 1] + b[i - 2] + b[i - 3]
for _ in range(0, int(input())):
    inp = int(input()) + 1
    print(b[inp] % z, a[inp] % z)

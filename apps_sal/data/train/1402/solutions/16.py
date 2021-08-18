t = int(input())
for j in range(t):
    a = int(input(), 2)
    b = int(input(), 2)
    i = 0
    while b > 0:
        u = a ^ b
        b = 2 * (a & b)
        a = u
        i += 1

    print(i)

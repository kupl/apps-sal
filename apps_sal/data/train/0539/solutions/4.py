t = eval(input())
for i in range(t):
    n = eval(input())
    m = n + 1
    l = 4 * n
    if (4 * n) % m == 0:
        print(4 * n / m)
    else:
        a = l
        b = m
        while b:
            a, b = b, a % b
        print(l / a)

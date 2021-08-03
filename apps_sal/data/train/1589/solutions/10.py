t = int(input())
for _ in range(t):
    l = list(map(int, input().strip().split()))
    l.insert(0, 0)
    c, n, a = 0, 0, 0
    for i in range(1, len(l)):
        if l[i] >= 30:
            c += 1
        if l[i] % 2 == 0:
            a += l[i] * i
            n += i
    x = a / n
    print(c, "{:.2f}".format(x))

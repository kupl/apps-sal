def divs(n):
    x = []
    i = 2
    while i <= n:
        if n % i == 0:
            x.append(i)
        i += 1
    return x


for _ in range(int(input())):
    (x, k) = map(int, input().split())
    xd = divs(x)
    kd = divs(k)
    (a, b) = (0, 0)
    for i in xd:
        a += pow(i, k)
    for i in kd:
        b += i * x
    print(a, b)

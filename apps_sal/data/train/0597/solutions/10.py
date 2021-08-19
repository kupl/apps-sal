for t in range(int(input())):
    x = []
    y = []
    z = []
    res = 0
    n = int(input(''))
    for i in range(n):
        (temp1, temp2) = input('').split()
        x.append(int(temp1))
        y.append(int(temp2))
    z.insert(0, x[1] - x[0])
    z.insert(-1, x[-1] - x[-2])
    for i in range(1, n - 1):
        z.insert(i, x[i + 1] - x[i - 1])
    y.sort(reverse=True)
    z.sort(reverse=True)
    for i in range(n):
        res = res + y[i] * z[i]
    print(res)

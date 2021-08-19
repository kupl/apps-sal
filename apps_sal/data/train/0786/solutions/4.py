t = int(input())
while t:
    t = t - 1
    n = int(input())
    x = bin(n)
    x = x[2:]
    x = x[::-1]
    z = 1
    s = 0
    for i in range(len(x)):
        if x[i] == '1':
            s += z
        z *= 6
    print(s)

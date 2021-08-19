# cook your dish here
xx = int(input(''))
for j in range(xx):
    a, b, c = list(map(int, input('').split()))
    x = list(map(int, input('').split()))
    t = 0
    k = 0
    z = 0
    for i in x:
        t = t + (i + k) // b
        k = k + i % b
        if t >= c:
            z = 1
            print(c)
            break
    if z == 0:
        print(t)

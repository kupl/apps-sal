for j in range(int(input())):
    r, g, b, m = map(int, input().split())
    x = []
    for i in range(3):
        a = list(map(int, input().split()))
        x.append(a)
    while(m != 0):
        c = []
        for i in x:
            c.append(max(i))
        z = c.index(max(c))
        for i in range(len(x[z])):
            x[z][i] = x[z][i] // 2
        m -= 1
    am = []
    for i in x:
        am += i
    print(max(am))

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    x = [int(i) for i in input().split()]
    y = 0
    z = 0
    l = 0
    k = 0
    d = {}
    for i in range(len(s)):
        if s[i] == '1':
            d[y] = i
            y = y + 1

    ln = y
    if(d[0] != 0):
        i = d[0]
        l = x[i] - x[0]

    for i in range(ln - 1):
        y = d[i]
        z = d[i + 1]
        max = -90
        for j in range(d[i] + 1, d[i + 1] + 1):
            if(max < (x[j] - x[j - 1])):
                max = x[j] - x[j - 1]

        l = l + (x[z] - x[y]) - max

    if(d[ln - 1] != n - 1):
        i = d[ln - 1]
        l = l + (x[n - 1] - x[i])

    print(l)

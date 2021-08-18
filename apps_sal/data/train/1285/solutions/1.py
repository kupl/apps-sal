t = int(input())

for _ in range(t):
    n = int(input())

    a = []
    for i in range(n):
        temp = [int(x) for x in input().split()]
        a.append(temp)

    trace = 0

    i = 0
    for j in range(n):
        r = i
        c = j

        m = a[r][c]

        while(r < n - 1 and c < n - 1):
            r += 1
            c += 1

            m += a[r][c]

        if(m > trace):
            trace = m

    i = 0
    for j in range(1, n):
        r = j
        c = i

        m = a[r][c]

        while(r < n - 1 and c < n - 1):
            r += 1
            c += 1

            m += a[r][c]

        if(m > trace):
            trace = m

    print(trace)

t = int(input())
for _ in range(t):
    n = int(input())
    l = [0] * n
    r = [0] * n
    for i in range(n):
        s = input()
        l[i] = s[:n // 2].count("1")
        r[i] = s[n // 2:].count("1")
        if(l[i] > r[i]):
            l[i] = l[i] - r[i]
            r[i] = 0
        elif(l[i] == r[i]):
            l[i] = 0
            r[i] = 0
        else:
            r[i] = r[i] - l[i]
            l[i] = 0
    lsum = sum(l)
    rsum = sum(r)
    x = abs(lsum - rsum)
    if(x == 0):
        print("0")

    else:
        m = 1000000000000000
        if(lsum > rsum):
            for j in range(n):
                k = abs(x - 2 * l[j])
                if(k < m):
                    m = k
                    if(m == 0):
                        break
        elif (rsum > lsum):
            for j in range(n):
                k = abs(x - 2 * r[j])
                if (k < m):
                    m = k
                    if (m == 0):
                        break
        print(m)

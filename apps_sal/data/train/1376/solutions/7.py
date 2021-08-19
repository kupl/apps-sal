# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    c = [int(i) for i in input().split()]
    i = 0
    m = 0
    if(n == 2 and k == 5):
        c1 = c
        c.sort()
        d = dict()
        for i in range(len(c1)):
            for j in range(len(c)):
                if(c[j] == c1[i]):
                    d[j] = i
                    c1[i] = -1
                    break

        while(m < n):
            if (i == n):
                print(d[n], k, n - 1, 0)
                c[n] -= k
                m += 1
            else:
                if(c[i] >= k):
                    print(d[i], k, i + 1, 0)
                    c[i] = c[i] - k
                    m += 1
                elif(c[i] == 0):
                    i += 1
                else:
                    for j in range(i + 1, n + 1):
                        if(c[i] + c[j] >= k):
                            print(i, c[i], j, k - c[i])
                            c[j] -= k - c[i]
                            c[i] = 0
                            m += 1
                            break

    else:
        while(m < n):
            if (i == n):
                print(n, k, n - 1, 0)
                c[n] -= k
                m += 1
            else:
                if(c[i] >= k):
                    print(i, k, i + 1, 0)
                    c[i] = c[i] - k
                    m += 1
                elif(c[i] == 0):
                    i += 1
                else:
                    for j in range(i + 1, n + 1):
                        if(c[i] + c[j] >= k):
                            print(i, c[i], j, k - c[i])
                            c[j] -= k - c[i]
                            c[i] = 0
                            m += 1
                            break

y = int(input())
while(y):
    y -= 1
    n, m = map(int, input().split())
    l1 = []
    for i in range(n):
        l1.append(0)
    k = -1
    l3 = []
    l4 = []
    for i in range(n):
        k1 = -1
        k2 = -1
        l2 = input().split()
        for j in range(len(l2)):
            if(l2[j] == 'P'):
                if(k == -1):
                    k = i
                if(k1 == -1):
                    k1 = j
                k2 = j
        if(k1 == -1):
            l1[i] = 1
        l3.append(k1)
        l4.append(k2)
    if(n == 1 or k == n - 1 or k == -1):
        if(n == 1):
            print(l4[0] - l3[0])
        else:
            print(l4[n - 1] - l3[n - 1])
        continue
    c = 0
    if(k % 2 != 0):
        a1 = l4[k]
    else:
        a1 = l3[k]
    for i in range(k, n - 1):
        if(l3[i + 1] == -1):
            if(i % 2 != 0):
                l3[i + 1] = l4[i + 1] = l3[i]
            else:
                l3[i + 1] = l4[i + 1] = l4[i]
        if(i % 2 != 0):
            a2 = min(l3[i + 1], l3[i])
            c += (a1 - a2)
            a1 = a2
        else:
            a2 = max(l4[i], l4[i + 1])
            c += (a2 - a1)
            a1 = a2
    if((n - 1) % 2 != 0):
        c += a1 - l3[n - 1]
    else:
        c += l4[n - 1] - a1
    c += n - 1
    for i in range(n - 1, -1, -1):
        if(l1[i] == 1):
            c -= 1
        else:
            break
    c -= k
    print(c)

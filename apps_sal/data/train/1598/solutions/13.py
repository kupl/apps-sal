t = int(input())
for i in range(t):
    n = int(input())
    l = []
    for j in range(n):
        l.append(input().split())
    sum = 0
    avg = 0
    for j in range(n):
        sum += int(l[j][2])
    avg = sum / n
    x = []
    for k in l:
        if int(k[2]) < avg:
            x.append(k[2])
    x.sort()
    y = 0
    le = len(x)
    while le != 0:
        for k in l:
            if y < len(x):
                if x[y] == k[2]:
                    print(k[0], k[1], k[2])
                    y += 1
                    le -= 1
                    k[2] = -1
                    break

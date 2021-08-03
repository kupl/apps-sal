t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        b.append([a[i], i])
    b = sorted(b, key=lambda R: R[0])
    positions = [0] * n
    for i in range(n):
        positions[b[i][1]] = i
    leftmin = []
    rightmin = []
    for i in range(n):
        leftmin.append(0)
        rightmin.append(0)
    for i in range(n - 1):
        for j in range(i + 1):
            if a[j] > a[i + 1]:
                l = positions[i + 1] + 1
                r = n - positions[j]
                for k in range(l - 1, -1, -1):
                    if leftmin[k] >= r:
                        break
                    leftmin[k] = r
                for k in range(r - 1, -1, -1):
                    if rightmin[k] >= l:
                        break
                    rightmin[k] = l
    maximum = n
    for i in range(n):
        maximum = min(maximum, leftmin[i] + i)
        maximum = min(maximum, rightmin[i] + i)
    print(maximum)

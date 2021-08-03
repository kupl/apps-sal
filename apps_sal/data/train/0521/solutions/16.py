import math
for i in range(int(input())):
    n = int(input())
    tmp = input().split()
    arr = []
    for j in tmp:
        arr.append(int(j))
    tmp = input().split()
    x = int(tmp[0])
    y = int(tmp[1])
    s = 0
    arr.sort()
    for j in range(int(n / 2)):
        d1 = (arr[j] - x)**2 + y**2
        d2 = (arr[n - j - 1] - x)**2 + y**2
        d3 = (arr[n - 1 - j] - arr[j])**2
        s += math.acos((d1 + d2 - d3) / (2 * math.sqrt(d1) * math.sqrt(d2)))
    print('{0:0.12}'.format(s))

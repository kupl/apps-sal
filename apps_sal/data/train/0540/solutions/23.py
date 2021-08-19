t = int(input())
while t > 0:
    t -= 1
    (n, m) = map(int, input().split())
    a = [int(x) for x in input().split()]
    count = 0
    temp = [0] * (m + 1)
    for i in range(n):
        if a[i] == m:
            temp[a[i]] += 1
        elif a[i] > m:
            pass
        else:
            temp[a[i]] = 1
    for i in range(1, m):
        if temp[i] == 0:
            print(-1)
            break
        if i == m - 1:
            print(n - temp[-1])

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    pre = []
    pre.append(arr[0])
    for i in range(1, n):
        pre.append(arr[i] + pre[i - 1])
    cnt = 0
    day = 0
    while cnt < n - 1:
        cnt += pre[cnt]
        day += 1
    print(day)

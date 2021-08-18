t = eval(input())
for _ in range(t):
    n, d = list(map(int, input().split()))
    a = list(map(int, input().split()))
    avg = sum(a) / n
    res = 0

    for i in range(n - d):
        if a[i] < avg:
            diff = avg - a[i]
            a[i] += diff
            a[i + d] -= diff
            res += diff
        elif a[i] > avg:
            diff = a[i] - avg
            a[i] -= diff
            a[i + d] += diff
            res += diff
    flag = True
    for i in range(n):
        if a[i] != avg:
            flag = False
            break

    if flag:
        print(res)
    else:
        print(-1)

t = int(input())
while t != 0:
    t = t - 1
    n = int(input())
    ans = 0
    for i in range(1, n + 1, 1):
        sum = 0
        for j in range(1, i + 1, 1):
            sum = sum + j
        s = sum - i
        sum = sum + s
        if i != n:
            ans = ans + 2 * sum * i
        else:
            ans = ans + sum * i
    print(ans)

try:
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(0)
    temp1 = [1 for i in range(n + 2)]
    k -= 1
    temp1[k] = 0
    temp1[k + 1] = temp1[k] + a[k + 1]
    for i in range(k + 2, n):
        temp1[i] = max(temp1[i - 2], temp1[i - 1])
        temp1[i] += a[i]
    temp2 = [1 for i in range(n + 2)]
    temp2[0] = a[0]
    temp2[1] = a[0] + a[1]
    for i in range(2, n):
        temp2[i] = max(temp2[i - 1], temp2[i - 2]) + a[i]
    ans = -1000000000
    for i in range(k, n):
        ans = max(ans, temp1[i] + temp2[i] - a[i])
    print(ans)
except:
    pass

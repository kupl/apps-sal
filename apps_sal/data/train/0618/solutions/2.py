for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    temp = list(map(int, input().split()))
    if n == k:
        print(sum(temp))
    elif n > k:
        l = len(temp)
        res = sum(temp[:k])
        s = sum(temp[:k])
        temp = temp[:] + temp[:k - 1]
        for i in range(l - 1):
            s = (s - temp[i]) + temp[k + i]
            if res < s:
                res = s
        print(res)

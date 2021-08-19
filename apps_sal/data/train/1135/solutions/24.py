try:
    test = int(input())
    while test > 0:
        (n, k) = map(int, input().split())
        a = []
        temp = k + 1
        if k == 0:
            a.append(n)
            for i in range(n - 1):
                a.append(i + 1)
        else:
            a.append(n - k)
            num = n - k + 1
            for _ in range(k):
                a.append(num)
                num += 1
            temp = n - k - 1
            for i in range(temp):
                a.append(i + 1)
        for num in a:
            print(num, end=' ')
        test -= 1
except:
    pass

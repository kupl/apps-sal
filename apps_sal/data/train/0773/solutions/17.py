t = int(input())
for _ in range(t):
    n = int(input())
    lis = [int(i) for i in range(n)]
    if n % 2 == 0:
        for i in range(n):
            if i % 2 == 0:
                lis[i] = i + 2
            else:
                lis[i] = i
    else:
        for i in range(n - 3):
            if i % 2 == 0:
                lis[i] = i + 2
            else:
                lis[i] = i
        (lis[n - 3], lis[n - 2], lis[n - 1]) = (n - 1, n, n - 2)
    for ele in lis:
        print(ele, end=' ')
    print('\n')

for _ in range(int(input())):
    (n, k) = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    ind = [[] for i in range(k)]
    for i in range(n):
        ind[a[i] - 1].append(i)
    maxi = 0
    flag = 0
    for i in ind:
        if len(i) == 0:
            flag = 1
            break
        maxi = max(maxi, i[0])
        for j in range(1, len(i)):
            maxi = max(i[j] - i[j - 1] - 1, maxi)
        maxi = max(n - i[-1] - 1, maxi)
    if flag == 1:
        print(n)
    else:
        print(maxi)

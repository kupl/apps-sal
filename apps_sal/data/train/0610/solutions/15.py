for test_ in range(int(input())):
    n = int(input())
    a = list(map(int, input().strip().split()))
    temp = []
    for i in range(n):
        if a[i] == 1:
            temp.append(i)
    if len(temp) == 1:
        print('YES')
    else:
        dist = []
        for i in range(1, len(temp)):
            dist.append(temp[i] - temp[i - 1])
        print('YES' if min(dist) >= 6 else 'NO')

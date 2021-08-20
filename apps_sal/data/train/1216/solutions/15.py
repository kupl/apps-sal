t = int(input())
i = 0
while i < t:
    y = input().split()
    n = int(y[0])
    x = int(y[1])
    a = input().split()
    m = 0
    while m < n:
        a[m] = int(a[m])
        m += 1
    j = 0
    while j < n:
        if a[j] >= x:
            print('YES')
            break
        elif j == n - 1 and a[j] < x:
            print('NO')
            break
        else:
            j = j + 1
    i = i + 1

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    has_true = True
    max_a = max(a)
    series1 = []
    series2 = []
    if a.count(max_a) > 1:
        print('NO')
        continue
    i = 0
    a.sort()
    while i < n:
        if a.count(a[i]) > 2:
            has_true = False
            print('NO')
            break
        if a.count(a[i]) == 2:
            series1.append(a[i])
            series2.append(a[i])
            i += 1
        else:
            series1.append(a[i])
        i += 1
    if has_true == True:
        series2 = series2[::-1]
        print('YES')
        print(*series1 + series2)

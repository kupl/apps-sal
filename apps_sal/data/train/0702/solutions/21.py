for i in range(int(input())):
    (m, a, b) = list(map(int, input().split()))
    d = abs(a - b)
    if d % 3 == 0 and d / 3 <= m:
        print('No')
    else:
        print('Yes')

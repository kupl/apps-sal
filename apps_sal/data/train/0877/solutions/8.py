for _ in range(int(input())):
    (x, y, k, n) = map(int, input().split())
    a = abs(x - y) / 2
    if a % k == 0:
        print('Yes')
    else:
        print('No')

for _ in range(int(input())):
    (x, y, k, n) = list(map(int, input().split()))
    if abs(x - y) % (2 * k) != 0:
        print('No')
    else:
        print('Yes')

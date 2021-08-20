for _ in range(int(input())):
    (x, y, k, n) = map(int, input().split())
    if abs(x - y) % k == 0:
        if abs(x - y) / k % 2 == 0:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

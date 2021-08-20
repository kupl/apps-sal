for q in range(int(input())):
    (x, y, k, n) = [int(z) for z in input().split()]
    a = max(x, y)
    b = min(x, y)
    if (a - b) / 2 % k == 0:
        print('Yes')
    else:
        print('No')

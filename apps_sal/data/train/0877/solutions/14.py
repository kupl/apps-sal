for _ in range(int(input())):
    (a, b, k, n) = map(int, input().split())
    val = abs(a - b)
    if val / k % 2 == 0:
        print('Yes')
    else:
        print('No')

for _ in range(int(input())):
    (n, k) = input().split()
    n = int(n)
    k = int(k)
    p = 2 ** n - 1
    if p == k:
        print('ON')
    elif p < k:
        if (k - p) % 2 ** n == 0:
            print('ON')
        else:
            print('OFF')
    else:
        print('OFF')

for i in range(int(input())):
    (n, k) = [int(i) for i in input().split()]
    if n % 2 == 0:
        if k < n * (n + 1) // 2 - 1 or k > 3 * (n // 2) ** 2 - 1:
            print(-1)
        elif k == n * (n + 1) // 2 - 1:
            for i in range(1, n + 1):
                print(i, '', end='')
            print()
        else:
            (k, count, p, l, x) = (k - n * (n + 1) // 2 + 1, 0, 0, [0 for i in range(n)], 1)
            while k > 0:
                p += 2
                (k, count) = (k - n + p, count + 1)
            for i in range(n, n - count + 1, -1):
                l[x] = i
                x += 2
            k = -k
            (l[2 * count - 1 + k], p) = (n - count + 1, 1)
            for i in range(n):
                if l[i] == 0:
                    l[i] = p
                    p += 1
            for i in l:
                print(i, '', end='')
            print()
    elif n == 1:
        print(1) if k == 0 else print(-1)
    elif k < n * (n + 1) // 2 - 1 or k > 3 * (n // 2) * (n // 2 + 1):
        print(-1)
    elif k == n * (n + 1) // 2 - 1:
        for i in range(1, n + 1):
            print(i, '', end='')
        print()
    else:
        (k, count, p, l, x) = (k - n * (n + 1) // 2 + 1, 0, 0, [0 for i in range(n)], 1)
        while k > 0:
            p += 2
            (k, count) = (k - n + p, count + 1)

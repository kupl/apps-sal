for _ in range(int(input())):
    n, p = list(map(int, input().split()))

    a = []
    ans = 0

    if n % p != 0 or p == 1 or p == 2:
        ans += 1

    if n == p:
        a = ['a'] * n

        if n % 2 == 0:
            a[n // 2] = 'b'
            a[n // 2 - 1] = 'b'
        else:
            a[n // 2] = 'b'

    else:
        if p % 3 == 0:
            k = n // 3
            for i in range(k):
                a.append('aba')

        elif p % 4 == 0:
            k = n // 4
            for i in range(k):
                a.append('abba')

        else:
            a = ['a'] * n

            if p % 2 == 0:
                for i in range(n // p):
                    a[p // 2 + i * p] = 'b'
                    a[p // 2 + i * p - 1] = 'b'

            else:
                for i in range(n // p):
                    a[p // 2 + i * p] = 'b'

    if ans > 0:
        print('impossible')
    else:
        print(''.join(a))

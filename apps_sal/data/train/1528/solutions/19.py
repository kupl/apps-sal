for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    a = list(input().split())
    while k > 0:
        if a[-1] == 'H':
            for i in range(len(a) - 1):
                if a[i] == 'H':
                    a[i] = 'T'
                else:
                    a[i] = 'H'
            a.pop()
        else:
            a.pop()
        k = k - 1
    print(a.count('H'))

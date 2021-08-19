for _ in range(int(input())):
    n = int(input())
    for i in range(n * 2 + 1):
        if i < n:
            s = ''
            s = s + (n - i) * ' '
            k = n
            for j in range(n - i, n + 1):
                s = s + str(k)
                k = k - 1
        elif i == n:
            s = ''
            for x in range(n, -1, -1):
                s = s + str(x)
        else:
            s = ''
            s = s + (i - n) * ' '
            k = n
            for j in range(i - n, n + 1):
                s = s + str(k)
                k = k - 1
        print(s)

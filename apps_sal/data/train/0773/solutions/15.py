from sys import stdin
try:
    t = eval(stdin.readline())
    for _ in range(t):
        n = eval(stdin.readline())
        arr = [x for x in range(1, n + 1)]
        if n % 2 == 0:
            for i in range(0, n - 1, 2):
                (arr[i], arr[i + 1]) = (arr[i + 1], arr[i])
        else:
            for i in range(0, n, 2):
                if i < n - 2:
                    (arr[i], arr[i + 1]) = (arr[i + 1], arr[i])
                else:
                    (arr[i], arr[i - 1]) = (arr[i - 1], arr[i])
        print(' '.join(list(map(str, arr))))
except:
    pass

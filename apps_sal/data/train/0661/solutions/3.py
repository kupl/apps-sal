try:
    (test, x) = map(int, input().split())
    for t in range(test):
        n = int(input())
        s = int(n ** 0.5)
        if n - s ** 2 <= n * x / 100:
            print('yes')
        else:
            print('no')
except:
    pass

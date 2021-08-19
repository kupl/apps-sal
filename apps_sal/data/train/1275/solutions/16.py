for t in range(int(input())):
    (n, m) = map(int, input().split())
    x = list(map(int, input().split()))
    max1 = max(x)
    min1 = min(x)
    for i in range(n):
        y = max(max1 - i, i - min1)
        print(y, end=' ')
    print()

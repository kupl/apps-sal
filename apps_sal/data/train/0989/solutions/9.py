n = int(input())
for _ in range(n):
    (x, y, k) = list(map(int, input().split()))
    sumxy = x + y
    div = sumxy // k
    rem = sumxy % k
    if div % 2 == 0:
        print('Chef')
    else:
        print('Paja')

for _ in range(int(input())):
    n = int(input())
    x = int(input())
    l = list(map(int, input().split()))
    l.sort()
    if n % x == 0:
        td = n // x
    else:
        td = n // x + 1
    for d in range(1, td + 1):
        if l[(d - 1) * x] == d:
            print('Impossible')
            break
    if l[(d - 1) * x] != d:
        print('Possible')

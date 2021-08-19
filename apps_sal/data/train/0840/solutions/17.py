t = int(input())
while t:
    n = int(input())
    for i in range(1, n + 1):
        if i == 1 or i == n:
            print('*')
            continue
        print(' ' * min(i - 1, n - i) + '*')
    t -= 1

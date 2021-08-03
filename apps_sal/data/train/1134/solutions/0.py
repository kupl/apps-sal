t = int(input())
for i in range(t):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    army = 0
    if n > m:

        for i in range(0, m):
            army += a[i]

        for j in range(m, n):
            army = army - (a[j] / 2)
            if army < 0:
                print('DEFEAT')
                break
            else:
                continue
        else:
            print('VICTORY')

    if n <= m:
        print('VICTORY')

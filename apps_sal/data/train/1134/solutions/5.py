x = eval(input())
while(x > 0):
    x -= 1
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    tot = 0
    ans = 1
    for i in range(m):
        tot += a[i]
    for i in range(m, n):
        tot -= (a[i] + 1) // 2
        if tot < 0:
            ans = 0
            print('DEFEAT')
            break
    if ans == 1:
        print('VICTORY')

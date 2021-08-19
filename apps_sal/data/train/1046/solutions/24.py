t = int(input())
for ts in range(t):
    (x, y) = map(int, input().split())
    a = 1
    b = 2
    while 1:
        if x < a:
            print('Bob')
            break
        elif y < b:
            print('Limak')
            break
        x -= a
        y -= b
        a += 2
        b += 2

t = int(input())
for i in range(t):
    (n1, n2) = map(int, input().split())
    b = 0
    l = 0
    c = 1
    while 1:
        if c % 2 == 0:
            l = l + c
        else:
            b = b + c
        if b > n1:
            print('Bob')
            break
        elif l > n2:
            print('Limak')
            break
        c = c + 1

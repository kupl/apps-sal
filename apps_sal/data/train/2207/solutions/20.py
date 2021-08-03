n = int(input())
na, nb, ca, cb = 0, 0, 0, 0
while n > 0:
    x, y, z = map(int, input().split())
    if x == 1:
        na += 10
        ca += y
    else:
        nb += 10
        cb += y
    n = n - 1
if ca * 2 >= na:
    print('LIVE')
else:
    print('DEAD')

if cb * 2 >= nb:
    print('LIVE')
else:
    print('DEAD')

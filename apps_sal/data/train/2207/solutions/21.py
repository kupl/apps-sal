def myprint(ca, na):
    if ca * 2 >= na:
        print('LIVE')
    else:
        print('DEAD')


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
myprint(ca, na)
myprint(cb, nb)

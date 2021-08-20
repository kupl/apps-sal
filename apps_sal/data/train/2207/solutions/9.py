n = int(input())
a = 0
a1 = 0
b = 0
b1 = 0
for i in range(n):
    (t, x, y) = list(map(int, input().split()))
    if t == 1:
        a += x
        a1 += y
    else:
        b += x
        b1 += y
if a >= a1:
    print('LIVE')
else:
    print('DEAD')
if b >= b1:
    print('LIVE')
else:
    print('DEAD')

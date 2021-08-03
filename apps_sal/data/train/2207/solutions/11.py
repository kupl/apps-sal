n = int(input())
ax = ay = bx = by = 0
for i in range(n):
    x, y, z = [int(t) for t in input().split()]
    if x == 1:
        ax += y
        ay += z
    else:
        bx += y
        by += z
print('LIVE' if ax >= ay else 'DEAD')
print('LIVE' if bx >= by else 'DEAD')

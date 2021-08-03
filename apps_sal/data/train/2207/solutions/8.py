n = int(input())
r = [[0, 0, 0], [0, 0, 0]]
for i in range(n):
    t, x, y = map(int, input().split())
    if t == 1:
        r[0][0] += 1
        r[0][1] += x
        r[0][2] += y
    else:
        r[1][0] += 1
        r[1][1] += x
        r[1][2] += y
for i in r:
    if i[1] < i[2]:
        print('DEAD')
    else:
        print('LIVE')

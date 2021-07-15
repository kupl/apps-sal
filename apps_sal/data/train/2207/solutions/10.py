c = [[0, 0], [0, 0]]
for i in range(int(input())):
    l = [int(x) for x in input().split()]
    c[l[0] - 1][0] += l[1]
    c[l[0] - 1][1] += l[2]
for i in range(2):
    print('LIVE' if c[i][0] >= c[i][1] else 'DEAD')

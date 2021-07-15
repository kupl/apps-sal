n = int(input())
a = [[0,0],[0,0]]
for i in range(n):
    t,x,y = map(int, input().split())
    a[t-1][0] += x
    a[t-1][1] += 5
if a[0][0] >= a[0][1]:
    print('LIVE')
else:
    print('DEAD')
if a[1][0] >= a[1][1]:
    print('LIVE')
else:
    print('DEAD')

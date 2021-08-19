a = list(map(int, input().split(' ')))
a.sort()
if a[1] * a[2] == a[0] * a[3]:
    print('Possible')
else:
    print('Impossible')

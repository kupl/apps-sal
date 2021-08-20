a = [int(x) for x in input().split()]
a.sort()
if a[0] * a[3] == a[2] * a[1]:
    print('Possible')
else:
    print('Impossible')

aa = []
for i in range(11):
    x = int(input())
    aa.append(x)
for x in aa[::-1]:
    a = x ** 3 * 5
    b = abs(x) ** 0.5
    ans = a + b
    if ans >= 400:
        print('f(' + str(x) + ') = MAGNA NIMIS!')
    else:
        print('f(' + str(x) + ') = ' + '%.2f' % ans)

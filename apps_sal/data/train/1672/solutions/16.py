t = []
while 1:
    try:
        x = int(input())
        t += [x]
    except:
        break
for x in t[::-1]:
    print('f(%d) = %s' % (x, '%.2f' % (5 * x**3 + abs(x)**.5)if x < 5 else'MAGNA NIMIS!'))

from math import sqrt
a = []
for i in range(11):
    a.append(int(input()))
for i in range(10, -1, -1):
    x = a[i]
    aresult = sqrt(abs(x))
    bresult = x * x * x * 5
    result = aresult + bresult
    print('f(' + str(x) + ') = ', sep='', end='')
    if result >= 400:
        print('MAGNA NIMIS!')
    else:
        print('%.2f' % result)

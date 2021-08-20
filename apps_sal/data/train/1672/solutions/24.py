s = [0] * 11
for i in range(11):
    s[i] = int(input())
for i in range(10, -1, -1):
    ares = abs(s[i]) ** 0.5
    bres = s[i] ** 3 * 5
    res = ares + bres
    if res < 400:
        print('f({}) = {:.2f}'.format(s[i], res))
    else:
        print('f({}) = MAGNA NIMIS!'.format(s[i]))

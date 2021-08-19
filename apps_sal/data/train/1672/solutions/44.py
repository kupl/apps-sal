a = []
for i in range(11):
    a.append(int(input()))
for i in range(11):
    x = a.pop()
    r = abs(x) ** 0.5 + x ** 3 * 5
    if r <= 400:
        print('f(%d) = %.2f' % (x, r))
    else:
        print('f(%d) = MAGNA NIMIS!' % x)

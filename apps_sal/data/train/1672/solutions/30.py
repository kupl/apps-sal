s = []
for i in range(11):
    s.append(int(input()))

for i in range(11):
    x = s.pop()
    a = abs(x) ** 0.5
    b = x ** 3 * 5
    if a + b < 400:
        print('f(%d) = %.2f' % (x, a + b))
    else:
        print('f(%d) = MAGNA NIMIS!' % x)


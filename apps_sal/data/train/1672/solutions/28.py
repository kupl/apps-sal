ls = []
for __ in range(11):
    ls.append(int(input()))
for x in reversed(ls):
    ans = 5 * x ** 3 + abs(x) ** 0.5
    if ans > 400:
        print('f({}) = MAGNA NIMIS!'.format(x))
    else:
        print('f({}) = {:.2f}'.format(x, ans))

stack = []
for _ in range(11):
    stack += (int(input()),)
while stack:
    v = stack.pop()
    a = abs(v) ** (1 / 2)
    b = v ** 3 * 5
    r = a + b
    if r > 400:
        print('f({}) = MAGNA NIMIS!'.format(v))
    else:
        print('f({}) = {:.2f}'.format(v, r))

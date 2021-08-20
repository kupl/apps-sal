import math
var = []
for i in range(11):
    t = int(input())
    var.append(t)
for i in range(11):
    d = var.pop()
    Ares = math.sqrt(abs(d))
    Bres = d ** 3 * 5
    res = Ares + Bres
    if res > 400:
        print(f'f({d}) = MAGNA NIMIS!')
    else:
        formatted = '{:.2f}'.format(res)
        print(f'f({d}) = {formatted}')

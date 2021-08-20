from itertools import product
(foo, rl) = (list(product('012', repeat=3)), 'RRRLRRLRRRLLR')
(bar, combos) = (list(rl + 'R' + rl[::-1]), dict())
for i in range(27):
    combos[foo[i]] = bar[i]


def elevator(l, r, c):
    return 'right' if combos[str(l), str(r), str(c)] == 'R' else 'left'

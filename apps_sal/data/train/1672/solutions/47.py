import math

def f(t):
    return math.sqrt(abs(t)) + 5 * t ** 3

a = [float(input()) for _ in range(11)]
for i, t in reversed(list(enumerate(a))):
    y = f(t)
    t = int(t)
    if y > 400:
        print(f'f({t}) = MAGNA NIMIS!')
    else:
        print(f'f({t}) =', '{:.2f}'.format(y))

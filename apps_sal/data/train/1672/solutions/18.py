from math import *
stack = []
for _ in range(11):
    stack.append(int(input()))
for i in range(11):
    var = stack.pop()
    a = sqrt(abs(var))
    b = var ** 3 * 5
    res = a + b
    if res <= 400:
        print(f'f({var}) = {res:.2f}')
    else:
        print(f'f({var}) = MAGNA NIMIS!')

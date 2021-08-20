import math
inp = []
for i in range(11):
    x = float(input())
    inp.append(x)
for x in reversed(inp):
    ans = math.sqrt(abs(x)) + x ** 3 * 5
    if ans > 400:
        print(f'f({int(x)}) = MAGNA NIMIS!')
    else:
        print(f'f({int(x)}) = {ans:.2f}')

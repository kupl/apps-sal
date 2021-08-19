from operator import __or__, __and__, __xor__
from sys import stdin, stdout
(n, b, c) = (int(stdin.readline()), 0, 1023)
m = {'|': __or__, '&': __and__, '^': __xor__}
for i in range(n):
    (t, v) = [i for i in stdin.readline().split()]
    b = m[t](b, int(v))
    c = m[t](c, int(v))
(x, o, a) = (0, 0, 1023)
for i in range(10):
    if b >> i & 1 and c >> i & 1:
        o |= 1 << i
    elif not b >> i & 1 and (not c >> i & 1):
        a -= 1 << i
    elif b >> i & 1 and (not c >> i & 1):
        x |= 1 << i
stdout.write('3\n| ' + str(o) + '\n^ ' + str(x) + '\n& ' + str(a))

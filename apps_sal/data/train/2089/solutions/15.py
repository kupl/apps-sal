from sys import stdin, stdout
from operator import __or__, __and__, __xor__
oper = {'&': __and__, '|': __or__, '^': __xor__}
n = int(stdin.readline())
a = 0
b = (1 << 10) - 1
for i in range(n):
    (op, x) = stdin.readline().split()
    x = int(x)
    a = oper[op](a, x)
    b = oper[op](b, x)
AND = (1 << 10) - 1
OR = 0
XOR = 0
for k in range(10):
    res0 = a & 1 << k
    res1 = b & 1 << k
    if not res0 and (not res1):
        AND ^= 1 << k
    elif not res0 and res1:
        pass
    elif res0 and (not res1):
        XOR ^= 1 << k
    else:
        OR ^= 1 << k
print(3)
print('& ', AND)
print('| ', OR)
print('^ ', XOR)

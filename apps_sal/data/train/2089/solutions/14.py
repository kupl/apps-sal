from sys import stdin, stdout

n = int(stdin.readline())
a = list()
y = 0

for i in range(n):
    oper, x = stdin.readline().split()
    x = int(x)
    a.append((oper, x))
    if oper == '&':
        y &= x
    elif oper == '|':
        y |= x
    elif oper == '^':
        y ^= x

AND = (1<<10) - 1
OR = 0
XOR = 0

for k in range(10):
    cur = 1 << k
    for comm in a:
        oper, x = comm
        if oper == '&':
            cur &= x
        elif oper == '|':
            cur |= x
        elif oper == '^':
            cur ^= x
    res0 = y & (1<<k)
    res1 = cur & (1<<k)
    if not res0 and not res1:
        AND ^= (1<<k)
    elif not res0 and res1:
        pass
    elif res0 and not res1:
        XOR ^= (1<<k)
    else:
        OR ^= (1<<k)

print(3)
print('& ', AND)
print('| ', OR)
print('^ ', XOR)




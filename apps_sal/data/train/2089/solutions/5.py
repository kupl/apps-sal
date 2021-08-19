import sys

n = int(sys.stdin.readline())
stat = [0] * 10  # 0: stay, 1: flip, 2: on, 3: off

for i in range(n):
    op, arg = sys.stdin.readline().split()
    arg = int(arg)

    if op == '&':
        for j in range(10):
            if arg & (1 << j) == 0:
                stat[j] = 3
    elif op == '|':
        for j in range(10):
            if arg & (1 << j) > 0:
                stat[j] = 2
    else:
        for j in range(10):
            if arg & (1 << j) > 0:
                stat[j] ^= 1

print('3')
orarg = 0
for i in range(10):
    if stat[i] == 2:
        orarg |= (1 << i)
print('| ' + str(orarg))

andarg = (1 << 10) - 1
for i in range(10):
    if stat[i] == 3:
        andarg ^= (1 << i)
print('& ' + str(andarg))

xorarg = 0
for i in range(10):
    if stat[i] == 1:
        xorarg += (1 << i)
print('^ ' + str(xorarg))

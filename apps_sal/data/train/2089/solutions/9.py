from sys import stdin

BITCOUNT = 10
xONES = (1 << 10) - 1
xZEROS = 0
n = int(stdin.readline())

for i in range(n):
    op, num = stdin.readline().split()
    num = int(num)
    if op == '&':
        xONES &= num
        xZEROS &= num
    elif op == '|':
        xONES |= num
        xZEROS |= num
    else:
        xONES ^= num
        xZEROS ^= num

andmask = 0
xormask = 0
mask = 1
for i in range(BITCOUNT):
    ONESbit = (xONES >> i) & 1
    ZEROSbit = (xZEROS >> i) & 1
    if (ONESbit == 1) and (ZEROSbit == 0):
        andmask += mask
    elif (ONESbit == 0) and (ZEROSbit == 1):
        andmask += mask
        xormask += mask
    elif (ONESbit == 1) and (ZEROSbit == 1):
        xormask += mask
    mask *= 2

print(2)
print('& {}'.format(andmask))
print('^ {}'.format(xormask))

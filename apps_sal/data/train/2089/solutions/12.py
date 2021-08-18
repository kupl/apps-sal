import sys
import heapq
import math
from enum import Enum


class Status:
    UNTOUCHED = 1
    FLIPPED = 2
    ONE = 3
    ZERO = 4


bits = [Status.UNTOUCHED] * 10
lines = sys.stdin.read().splitlines()

n = int(lines[0])

andNum = 1023
orNum = 0
xorNum = 0
for i in range(1, n + 1):

    operation, num = lines[i].split(' ')
    num = int(num)
    if operation == '|':
        andNum = andNum | num
        orNum = orNum | num
        xorNum = xorNum & (orNum ^ 1023)
    elif operation == '&':
        andNum = andNum & num
        orNum = orNum & num
        xorNum = xorNum & num
    else:
        oldAndNum = andNum
        oldOrNum = orNum
        andNum = andNum ^ ((orNum | (andNum ^ 1023)) & num)
        orNum = orNum ^ (((oldAndNum ^ 1023) | (orNum)) & num)
        xorNum = xorNum ^ (oldAndNum & (oldOrNum ^ 1023) & num)

print(3)
print('& ' + str(andNum))
print('| ' + str(orNum))
print('^ ' + str(xorNum))

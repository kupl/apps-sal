from collections import deque
import math
numbers = deque()
for _ in range(11):
    numbers.append(int(input()))
for _ in range(11):
    num = numbers.pop()
    a = math.sqrt(abs(num))
    b = num ** 3 * 5
    res = a + b
    if res < 400:
        print('f(%d) = %.2f' % (num, res))
    else:
        print('f(%d) = MAGNA NIMIS!' % num)

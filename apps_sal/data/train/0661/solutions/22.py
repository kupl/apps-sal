import math
(t, n) = input().split()
t = int(t)
n = int(n)
for _ in range(t):
    num = eval(input())
    num = int(num)
    sq = int(math.sqrt(num))
    squ = sq * sq
    diff = 0.01 * n * num
    if num - squ <= diff:
        print('yes')
    else:
        print('no')

from math import sqrt, ceil
import time
from bisect import bisect_right
start_time = time.time()

a = []
x = 0
y = 0
while x <= 10 ** 9:
    x = int(sqrt(y)) + 1
    a.append(x)
    y += x * x

end_time = time.time()

for _ in range(int(input())):
    n = int(input())
    print(bisect_right(a, n))

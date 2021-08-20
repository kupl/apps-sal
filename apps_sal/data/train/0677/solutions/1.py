import sys
from datetime import date
(a, b, c) = list(map(int, sys.stdin.readline().split()))
d = date(c, b, a)
print(d.strftime('%A'))

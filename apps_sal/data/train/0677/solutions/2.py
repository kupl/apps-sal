import sys
from datetime import date
a, b, c = list(map(int, sys.stdin.readline().split()))
day = date(c, b, a)
print(day.strftime("%A"))



import fractions
import sys

f = sys.stdin

if len(sys.argv) > 1:
 f = open(sys.argv[1], "rt")

def calc(rows):
 min_x = 10000
 min_y = 10000
 max_x = -1
 max_y = -1

 count = 0
 for y, row in enumerate(rows):
  for x, ch in enumerate(row):
   if ch == '*':
    count += 1
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    max_x = max(max_x, x)
    max_y = max(max_y, y)

 if count == 0:
  return 0
 return 1 + max(max_x - min_x + 1, max_y - min_y + 1) // 2

T = int(f.readline().strip())

for case_id in range(1, T+1):
 n, m = list(map(int, f.readline().strip().split()))

 rows = []
 for i in range(n):
  rows.append(f.readline().strip())

 r = calc(rows)

 print(r)


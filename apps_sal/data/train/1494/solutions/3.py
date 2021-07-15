#!/usr/bin/env python
import sys

boxes_number = int(sys.stdin.readline().rstrip())
boxes_sizes = list(map(int, sys.stdin.readlines()))

boxes_sizes.sort()

lower_bound, upper_bound = 0, boxes_number // 2 + 1

while lower_bound + 1 < upper_bound:
  middle = (lower_bound + upper_bound) >> 1

  possible = not middle or all(
    2 * boxes_sizes[i] <= boxes_sizes[boxes_number - middle + i]
    for i in range(middle)
  )

  if not possible:
    upper_bound = middle
  else:
    lower_bound = middle

print(boxes_number - lower_bound)


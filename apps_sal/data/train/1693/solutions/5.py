import sys
import math
count = int(sys.stdin.readline())
for i in range(count):
    numbers = list(map(int, sys.stdin.readline().split(' ')))
    n = len(numbers)
    total = sum(numbers)
    mean = total * 1.0 / n
    inside = 0
    for number in numbers:
        position = number / mean
        if position >= 0.5 and position <= 1.5:
            inside += 1
    if inside > 0.7 * n:
        print('poisson')
    else:
        print('uniform')

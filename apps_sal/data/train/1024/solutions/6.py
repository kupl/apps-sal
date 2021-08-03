# cook your dish here
from math import pow
check_possible = 0
for _ in range(int(input())):
    s, n, k, r = map(int, input().split())
    if r > 1:
        total_slices = k * (pow(r, n) - 1) / (r - 1)
    else:
        total_slices = k * n
    left_slices = s - total_slices
    check_possible += left_slices
    if left_slices >= 0:
        print('POSSIBLE', int(left_slices))
    else:
        print('IMPOSSIBLE', int(-(left_slices)))
if check_possible >= 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')

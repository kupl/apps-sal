import math
import bisect
t = int(input())
while t != 0:
    t -= 1
    n = int(input())
    candies = [int(x) for x in input().split()]
    rate = int(input())
    leftover = 0
    a_start_time = [0 for x in range(n)]
    b_start_time = [0 for x in range(n)]
    a_start_time[0] = 0
    b_start_time[-1] = 0
    sum_candies = candies[0]
    for i in range(1, n):
        a_start_time[i] = sum_candies // rate
        sum_candies += candies[i]
    for i in range(n - 2, -1, -1):
        b_start_time[i] = b_start_time[i + 1] + candies[i + 1]
    a_count = 0
    b_count = 0
    if n == 1:
        print(1, 0)
        continue
    elif n == 2:
        print(1, 1)
        continue
    for i in range(n):
        if a_start_time[i] < b_start_time[i]:
            a_count += 1
        elif b_start_time[i] < a_start_time[i]:
            b_count += 1
        elif a_count < n - a_count - 1:
            b_count += 1
        else:
            a_count += 1
    print(a_count, n - a_count)

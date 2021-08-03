import sys
import math


def solution():
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())
        cost_of_flavour = list(map(int, input().strip().split(' ')))
        cost_of_flavour = sorted(cost_of_flavour)
        w, y = list(map(int, input().strip().split(' ')))

        if y > w or y > n:
            print("Not Possible")
            continue
        else:
            min_sum = 0
            for i in range(y):
                min_sum += cost_of_flavour[i]
            min_sum += cost_of_flavour[0] * (w - y)
            print("%d" % (min_sum))


solution()

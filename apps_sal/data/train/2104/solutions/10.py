import math

x = int(input())

if (x == 1):
    print(0)
else:
    y = [int(x) for x in input().split(' ')]
    y.sort()
    x1 = y[0]
    y2 = y[-1]
    if (x % 2 == 1):
        case_1 = (y[x] - x1) * (y2 - y[x + 1])
    else:
        case_1 = (y[x - 1] - x1) * (y2 - y[x])

    case_2 = (y[-1] - y[0])
    start = 1
    end = start + x - 1
    minValue = y[end] - y[start]
    while (end < len(y) - 1):
        val = y[end] - y[start]
        if (val < minValue):
            minValue = val
        start += 1
        end += 1

    case_2 *= minValue

    print(min(case_1, case_2))

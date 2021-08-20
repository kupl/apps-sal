from datetime import date
from calendar import month_name


def solve(a, b):
    (m, c, res, s) = ([1, 3, 5, 7, 8, 10, 12], 0, [], '')
    for i in range(a, b + 1):
        for j in m:
            if date(i, j, 1).weekday() == 4:
                res.append(j)
                c += 1
                s = ''
    return (month_name[res[0]][:3], month_name[res[-1]][:3], c)

from datetime import *


def solve(a, b):
    ans = []
    for i in range(a, b + 1):
        for j in (1, 3, 5, 7, 8, 10, 12):
            start = date(i, j, 1)
            if start.strftime("%a") == "Fri":
                ans.append(start.strftime("%b"))
    return (ans[0], ans[-1], len(ans))

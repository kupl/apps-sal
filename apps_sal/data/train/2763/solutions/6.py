# x ^ 2 - 4 * y ^ 2 = A
import math


def sol_equa(n):
    ls = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            ls.append(i)
    ans = []
    for root in ls:
        x = int(((root + int(n / root)) / 2))
        y = int((max(root, int(n / root)) - x) / 2)
        if int(x + 2 * y) * (x - 2 * y) == n:
            ans.append([x, y])
    return ans

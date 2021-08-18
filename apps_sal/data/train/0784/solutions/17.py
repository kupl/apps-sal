import sys

n, m, p = list(map(int, sys.stdin.readline().split()))

d1 = {}

for i in range(p):
    i, j = list(map(int, sys.stdin.readline().split()))
    if i not in d1:
        d1[i] = {}
        d1[i][j] = 1
    else:
        if j not in d1[i]:
            d1[i][j] = 1
        else:
            d1[i][j] += 1


def matrix(n, m, d):
    ans = m - 1
    l = list(reversed(sorted(d.keys())))
    for i in range(len(l)):
        number = l[i]
        if number > 1:
            below = number - 1
        else:
            if len(l) == 1:
                if d[1] > 1:
                    return -1
                else:
                    return m - 2
            else:
                value = 1 + d[1]
                if 2 not in d:
                    if 2 - value >= 0:
                        ans += 2 - value - 1
                    else:
                        return -1
                return ans
        if number < m:
            above = number + 1
        else:
            if len(l) == 1:
                return ((m + d[m]) - (m - 1) - 1) + ans
            else:
                if m - 1 not in d:
                    ans += (m + d[m]) - (m - 1) - 1
                else:
                    below = (m - 1) + d[below]
                    value = m + d[m]
                    if value - below < 0:
                        return -1
                    else:
                        ans += value - (below) - 1
                continue
        value = number + d[number]
        if below in d:
            initial = below + d[below]
        else:
            initial = below
        if above in d:
            final = above + d[above]
        else:
            final = above
        if value - initial >= 0:
            ans += value - initial - 1
        else:
            return -1
        if len(l) == 1:
            if final - value >= 0:
                ans += final - value - 1
            else:
                return -1
        elif number + 1 != l[i - 1]:
            if final - value >= 0:
                ans += final - value - 1
            else:
                return -1

    return ans


for i in range(1, n + 1):
    if m == 1:
        print(0)
    elif i not in d1:
        print(m - 1)
    else:
        print(matrix(n, m, d1[i]))

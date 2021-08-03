from math import floor, sqrt

n = int(input())
for i in range(n):
    m = int(input())
    if m % 4 == 1 or m % 4 == 2:
        print(0)
    else:
        s = m * (m + 1) // 2
        res = 0
        sm = s // 2
        p1 = floor((sqrt(4 * s + 1) - 1) / 2)
        s1 = p1 * (p1 + 1) // 2
        p = [p1 - 1, p1, p1 + 1]
        s = [s1 - p1, s1, s1 + p[2]]
        l = [sm - s[0], sm - s1, sm - s[2]]
        for j in range(len(l)):
            if l[j] == 0:
                res += (p[j] * (p[j] - 1) + (m - p[j] - 1) * (m - p[j])) // 2
            elif l[j] > 0 and l[j] < m:
                res += min([l[j], m - l[j], p[j], m - p[j]])

        print(res)

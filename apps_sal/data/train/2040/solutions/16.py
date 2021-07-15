from math import sqrt
n, h = [int(x) for x in input().split()]
area = 1 * h / 2 / n
x = sqrt(2*area/h)
res = [x*h]
cur_area = area
for i in range(2, n):
    cur_area += area
    x = sqrt(2*cur_area/h)
    res.append(x*h)
print(res[0], end=" ")
for i in range(1, len(res)):
    print(" " + str(res[i]), end="")
print()

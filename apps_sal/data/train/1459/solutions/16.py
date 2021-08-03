import math


n, m = map(int, input().split())
hyp = math.sqrt(1 + m * m)
cosx = 1 / hyp
sinx = m / hyp

for i in range(n):
    px, py = list(map(int, input().strip().split()))
    px_temp = cosx * px + sinx * py
    py_temp = cosx * py - sinx * px

    if i == 0:
        px_max = px_temp
        px_min = px_temp
        py_max = py_temp
        py_min = py_temp

    if px_temp > px_max:
        px_max = px_temp
    elif px_temp < px_min:
        px_min = px_temp

    if py_temp > py_max:
        py_max = py_temp
    elif py_temp < py_min:
        py_min = py_temp

w = px_max - px_min
l = py_max - py_min

print(2 * l + 2 * w)

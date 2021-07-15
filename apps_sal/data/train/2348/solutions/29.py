3.6
import bisect
n = int(input())
x = [int(item) for item in input().split()]
l = int(input())
q = int(input())
ab = []
for i in range(q):
    a, b = [int(item) for item in input().split()]
    a -= 1; b -= 1
    if a > b:
        a, b = b, a
    ab.append((a, b))

dt = [[0] * n for _ in range(40)]
for i, item in enumerate(x):
    dt[0][i] = i
    dt[1][i] = bisect.bisect_right(x, item + l) - 1

for i in range(2, 40):
    for j in range(n):
        dt[i][j] = dt[i-1][dt[i-1][j]]

for a, b in ab:
    days = 0
    is_ok = False
    while a < b:
        for i in range(0, 40):
            if dt[i][a] >= b:
                if i == 1:
                    days += 1
                    is_ok = True
                else:
                    a = dt[i-1][a]
                    days += 2**(i-2)
                break
        if is_ok:
            break
    print(days)

import numpy as np


def PolyArea(x, y):
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


n = int(input())
a = []
b = []
for i in range(0, n):
    a1, b1 = input().split(" ")
    a1, b1 = int(a1), int(b1)
    a.append(a1)
    b.append(b1)
a1 = []
b1 = []
for i in range(0, n - 1):
    a1.append((a[i] + a[i + 1]) / 2)
    b1.append((b[i] + b[i + 1]) / 2)
a1.append((a[0] + a[-1]) / 2)
b1.append((b[0] + b[-1]) / 2)
print(PolyArea(np.array(a1), np.array(b1)))

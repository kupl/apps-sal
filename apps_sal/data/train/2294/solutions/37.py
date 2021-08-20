import numpy as np
import sys
input = sys.stdin.readline
N = int(input())
XY = np.array([input().split() for _ in range(N)], dtype=np.int64)
(X, Y) = XY.T
Z = X + Y
np.minimum(X, Y, out=X)
Y = Z - X
answer = (X.max() - X.min()) * (Y.max() - Y.min())
red = Y.max() - X.min()
idx = X.argsort()
X = X[idx]
Y = Y[idx]
Y_min = np.minimum.accumulate(Y)
Y_max = np.maximum.accumulate(Y)
a = Y_max[-1] - Y_min[-1]
b = (np.maximum(Y_max[:-1], X[-1]) - np.minimum(X[1:], Y_min[:-1])).min()
c = X[-1] - X[0]
answer = min(answer, red * min(a, b, c))
print(answer)

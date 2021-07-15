import sys
input = sys.stdin.readline

# 最大値が赤であるとしてよい

import numpy as np
N = int(input())
XY = np.array([input().split() for _ in range(N)], dtype = np.int64)
X,Y = XY.T
# X \leq Y に変換
Z = X+Y
np.minimum(X,Y,out=X)
Y = Z - X

# 最大のものを赤、最小のものを青とする
# この場合、任意の箱に対して、大きい方を赤、小さい方を青
answer = (X.max() - X.min()) * (Y.max() - Y.min())

red = Y.max() - X.min()
# 青の最小値を決めると全部決まる
# 小さい側でソート -> 左からいくつかを上側、右からいくつかを下側
idx = X.argsort()
X = X[idx]
Y = Y[idx]
Y_min = np.minimum.accumulate(Y)
Y_max = np.maximum.accumulate(Y)
a = Y_max[-1] - Y_min[-1] # 全部上側からとった場合
b = (np.maximum(Y_max[:-1], X[-1]) - np.minimum(X[1:],Y_min[:-1])).min() # 途中まで上側
c = X[-1] - X[0] # 全部下側
answer = min(answer, red * min(a,b,c))

print(answer)

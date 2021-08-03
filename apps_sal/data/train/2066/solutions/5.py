from itertools import accumulate
m = int(input()) // 2
X = [int(x) for x in input().split()]
X.sort()
Z = [X[i + m] - X[i] for i in range(m)]
print(min(Z))

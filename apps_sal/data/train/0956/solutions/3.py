def polygonArea(X, Y, n):
    area = 0.0
    j = n - 1
    for i in range(0, n):
        area += (X[j] * Y[i] - Y[j] * X[i])
        j = i
    return (abs(area / 2.0))


X = []
Y = []
xy = []
n = int(input())
for i in range(n):
    xy.append(list(map(int, input().split())))
for i in range((n - 1)):
    X.append((xy[i][0] + xy[i + 1][0]) / 2)
    Y.append((xy[i][1] + xy[i + 1][1]) / 2)
X.append((xy[0][0] + xy[n - 1][0]) / 2)
Y.append((xy[0][1] + xy[n - 1][1]) / 2)
print(polygonArea(X, Y, n))

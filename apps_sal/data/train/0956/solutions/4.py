x = []
y = []
n = int(input())
for i in range(n):
    a, b = list(map(int, input().split()))
    x.append(a)
    y.append(b)
a, b = [], []
for i in range(-1, n - 1):
    a.append((x[i] + x[i + 1]) / 2)
    b.append((y[i] + y[i + 1]) / 2)


def polygonArea(X, Y, n):

    area = 0.0

    j = n - 1
    for i in range(n):
        area += (X[j] + X[i]) * (Y[j] - Y[i])
        j = i
    return abs(area / 2)


print(polygonArea(a, b, n))

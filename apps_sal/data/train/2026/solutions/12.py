def R():
    return map(int, input().split())


(n, d) = R()
a = [0] + list(R()) + [0]
x = []
y = []
INF = float('inf')


def distance(x1, y1, x2, y2):
    return (abs(x1 - x2) + abs(y1 - y2)) * d


for i in range(n):
    (xi, yi) = R()
    x += [xi]
    y += [yi]
b = [INF] * n
b[0] = 0
c = True
while c:
    c = False
    for i in range(n):
        for j in range(1, n):
            if i != j and b[i] != -1:
                t = b[i] + distance(x[i], y[i], x[j], y[j]) - a[j]
                if t < b[j]:
                    b[j] = t
                    c = True
print(b[-1])

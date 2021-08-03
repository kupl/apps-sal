n, d = map(int, input().split())
a = [0] + list(map(int, input().split())) + [0]
x = []
y = []
for i in range(n):
    xx, yy = map(int, input().split())
    x += [xx]
    y += [yy]
b = [-1] * n
b[0] = 0
c = True
while c:
    c = False
    for i in range(n):
        for j in range(1, n):
            if i != j and b[i] != -1:
                t = b[i] + (abs(x[i] - x[j]) + abs(y[i] - y[j])) * d - a[j]
                if b[j] == -1 or t < b[j]:
                    b[j] = t
                    c = True
print(b[-1])

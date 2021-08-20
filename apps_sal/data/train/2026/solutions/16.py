(n, d) = list(map(int, input().split()))
a = [0] + list(map(int, input().split())) + [0]
X = []
Y = []
for i in range(n):
    (x, y) = list(map(int, input().split()))
    X.append(x)
    Y.append(y)
mon = [-1] * n
mon[0] = 0
Z = 0
while Z == 0:
    Z = 1
    for i in range(n):
        for j in range(1, n):
            if i != j and mon[i] != -1:
                costo = mon[i] + (abs(X[i] - X[j]) + abs(Y[i] - Y[j])) * d - a[j]
                if mon[j] == -1 or costo < mon[j]:
                    mon[j] = costo
                    Z = 0
print(mon[-1])

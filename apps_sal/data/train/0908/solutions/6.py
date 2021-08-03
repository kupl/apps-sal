r = int(input())
L = []
for i in range(r):
    x = int(input())
    L.append(x)
for i in range(r):
    print(int((((8 * L[i] + 1)**0.5) - 1) / 2))

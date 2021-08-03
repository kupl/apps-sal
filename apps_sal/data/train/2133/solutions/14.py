n = int(input())
y = [0] * 100
a = 0
for i in range(n):
    x = input()
    n = len(x)
    for j in range(n):
        y[j] = y[j] + int(x[j])
print(max(y))

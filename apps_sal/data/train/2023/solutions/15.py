import math
n = int(input())
k = math.ceil(n ** 0.5)
a = []
i = 1
while n - i * k > 0:
    for j in range(1, k + 1):
        a.append(str(n - i * k + j))
    i += 1
for l in range(1, n - (i - 1) * k + 1):
    a.append(str(l))
print(' '.join(a))

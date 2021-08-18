import math
a, b = list(map(int, input().split()))
l = []
m = []
for i in range(1, a + 1):
    l.append(i * i)
for i in range(1, b + 1):
    m.append(i)
cnt = 0
for i in range(a):
    for j in range(b):
        y = l[i] + m[j]
        if math.sqrt(y) == math.floor(math.sqrt(y)):
            cnt += 1
print(cnt)

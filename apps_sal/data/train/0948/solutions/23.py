import math
(a, b) = list(map(int, input().split()))
l = []
m = []
cnt = 0
for i in range(1, a + 1):
    for j in range(1, b + 1):
        y = i ** 2 + j
        if math.sqrt(y) == math.floor(math.sqrt(y)):
            cnt += 1
print(cnt)

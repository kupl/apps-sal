import sys
import random
n, m, c = list(map(int, input().split()))
max = []
li = []
options = []
for i in range(1, 51):
    print(1, 1, n, 1, m, i, i)
    sys.stdout.flush()
    ans = int(input())
    max.append(ans)
    li.append(ans)
max.sort()
max = max[::-1]

for i in range(5):
    options.append(li.index(max[i]) + 1)

print(3)
for i in range(n):
    for j in range(m - 1):
        print(random.choice(options), end=' ')

    print(random.choice(options))

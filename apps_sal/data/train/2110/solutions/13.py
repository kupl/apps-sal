import math
n = int(input())
w = [int(i) for i in input().split()]
mxN = 1000000 + math.ceil(math.log2(1000000)) + 1
btStr = [0] * mxN
for i in w:
    btStr[i] += 1
steps = 0
for i in range(mxN - 1):
    btStr[i + 1] += btStr[i] // 2
    btStr[i] = btStr[i] % 2
    steps += btStr[i]
print(steps)

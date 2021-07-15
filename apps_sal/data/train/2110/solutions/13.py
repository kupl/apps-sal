import math

n = int(input())

w = [int(i) for i in input().split()]
# w = [1000000] * 1000000
mxN = 1000000 + math.ceil(math.log2(1000000)) + 1

btStr = [0] * mxN

# print(btStr)
# mx = 0

for i in w:
    btStr[i] += 1
    # print(j)

# print(mx)
steps = 0

for i in range(mxN - 1):
    btStr[i + 1] += btStr[i] // 2
    btStr[i] = btStr[i] % 2
    steps += btStr[i]

# for i in btStr:
#     if i == 1:
#         steps += 1
#
print(steps)


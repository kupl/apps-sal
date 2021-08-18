N = int(input())

array = list(map(int, input().split()))

res = [0 for i in range(N + 1)]
stack = [(0, -1)]

for (i, height) in enumerate(array):
    while stack[-1][0] >= height:
        num = stack[-1][0]
        stack.pop()
        length = i - stack[-1][1] - 1
        res[length] = max(res[length], num)

    stack.append((height, i))

while len(stack) > 1:
    num = stack[-1][0]
    stack.pop()
    length = N - stack[-1][1] - 1
    res[length] = max(res[length], num)

for i in range(N - 1, 0, -1):
    res[i] = max(res[i], res[i + 1])

print(' '.join(map(str, res[1:])))

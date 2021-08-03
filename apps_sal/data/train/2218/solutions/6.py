n = int(input())
array = list(map(int, input().split()))
q = int(input())
d = {i: 0 for i in range(n)}
stack = []
for i in range(q):
    req = list(map(int, input().split()))
    if req[0] == 2:
        stack.append((req[1], i))
    else:
        p = req[1] - 1
        d[p] = i
        array[p] = req[2]
ans_i = [-1] * q
j = len(stack) - 1
max_of_stack = -1
for i in range(q - 1, -1, -1):
    if j > -1 and stack[j][1] >= i:
        max_of_stack = max(max_of_stack, stack[j][0])
        j -= 1
    ans_i[i] = max_of_stack
for p in range(n):
    if array[p] < ans_i[d[p]]:
        array[p] = ans_i[d[p]]
print(*array)

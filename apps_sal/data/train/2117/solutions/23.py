
n = int(input())
a = [int(o) for o in input().split()]
l = [-1] * n
r = [(n)] * n
stack = []
for i in range(n):
    while stack and a[stack[-1]] >= a[i]:
        stack.pop()
    if stack:
        l[i] = stack[-1]
    stack.append(i)
stack = []
for i in range(n - 1, -1, -1):
    while stack and a[stack[-1]] >= a[i]:
        stack.pop()
    if stack:
        r[i] = stack[-1]
    stack.append(i)
answers = [min(a)] * n

for i in range(n):
    lw = r[i] - l[i] - 2

    answers[lw] = max(answers[lw], a[i])

ans = min(a)
answers[0] = max(a)
for i in range(n - 1, -1, -1):
    ans = max(ans, answers[i])
    answers[i] = ans
print(*answers)

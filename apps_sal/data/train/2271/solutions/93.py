n, m = list(map(int, input().split()))
p = list(map(int, input().split()))
num = [[] for _ in range(n)]
for i in range(m):
    x, y = list(map(int, input().split()))
    num[x - 1].append(y)
    num[y - 1].append(x)
seen = [False] * n
ans = list(range(n))
for i in range(n):
    if seen[i] == False:
        queue = [i]
        seen[i] = True
        for j in range(n):
            if len(queue) == 0:
                break
            num1 = queue.pop()
            ans[num1] = i
            for k in range(len(num[num1])):
                num2 = num[num1][k] - 1
                if seen[num2] == False:
                    queue.append(num2)
                    seen[num2] = True
ans2 = 0
for i in range(n):
    if ans[i] == ans[p[i] - 1]:
        ans2 += 1
print(ans2)

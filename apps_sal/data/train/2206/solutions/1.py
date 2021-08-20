n = int(input())
p = list(map(int, input().split()))
lp = n + 1
ans = [1]
vis = [0 for i in range(n)]
ans = [1]
top = n
hardness = 1
for i in range(len(p)):
    vis[p[i] - 1] = 1
    hardness += 1
    while vis[top - 1] == 1 and top > 0:
        top -= 1
        hardness -= 1
    ans.append(hardness)
print(' '.join([str(i) for i in ans]))

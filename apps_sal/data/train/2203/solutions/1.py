n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
ans = []
for i in arr:
    anf = max(i)
    while (anf in ans):
        anf += 1
    ans.append(anf)
print(*ans)

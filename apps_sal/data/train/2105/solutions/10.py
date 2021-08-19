n = int(input())
ans = [1 for _ in range(n + 2)]
for i in range(2, int(n ** 0.5) + 2):
    if ans[i] == 2:
        continue
    for j in range(i * 2, n + 2, i):
        ans[j] = 2
print(len(set(ans)))
print(*ans[2:])

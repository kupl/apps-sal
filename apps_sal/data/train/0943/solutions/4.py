t = int(input())
ans = []
for _ in range(t):
    u, v = list(map(int, input().split()))
    ans.append(min(u, v) + 1)
for i in ans:
    print(i)

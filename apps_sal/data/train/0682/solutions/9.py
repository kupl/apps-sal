n = int(input())
coins = list(map(int, input().split()))
start = -1
end = -1
ans = [0 for x in range(n)]
for i in range(n):
    if coins[i] != i + 1:
        if start == -1:
            start = i
            break
    ans[i] = coins[i]

for i in range(n - 1, -1, -1):
    if coins[i] != i + 1:
        if end == -1:
            end = i
            break
    ans[i] = coins[i]
mid = start + (end - start) // 2
s = start
e = end
while s <= end:
    ans[s] = coins[e]
    s += 1
    e -= 1

start += 1
end += 1
for i in range(n):
    if ans[i] != i + 1:
        start = 0
        end = 0
        break
print(start, end)

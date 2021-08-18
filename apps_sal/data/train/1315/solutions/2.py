n = int(input())
ans = {}
count = 0
for _ in range(n):
    arr = list(map(int, input().split()))
    temp = sum(arr)
    if temp in ans:
        ans[temp] += 1
    else:
        ans[temp] = 1
count = 0
for i in list(ans.values()):
    if i == 1:
        count += 1
print(count)

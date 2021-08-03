n = int(input())
a = list(map(int, input().rstrip().split()))
ans = []
for i in a:
    if i == 2:
        ans.append(1)
    else:
        ans.append(i ^ 2)
print(*ans)

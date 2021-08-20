n = int(input())
a = list(map(int, input().split()))
b = [[i] for i in a]
for j in range(n):
    for i in range(1 << n):
        if i & 1 << j:
            b[i] = sorted(b[i] + b[i ^ 1 << j], reverse=True)[:2]
ans = []
tmp = 0
for i in range(1, 1 << n):
    tmp = max(tmp, sum(b[i]))
    ans.append(tmp)
print(*ans, sep='\n')

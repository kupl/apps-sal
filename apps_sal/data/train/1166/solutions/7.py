n = int(input())
lis = list(map(int, input().split()))
q = int(input())
ans = []
res = []
for i in range(len(lis) + 1):
    ans = []
    for j in range(i + 1, len(lis) + 1):
        ans = lis[i:j]
        res.append(ans)
while q > 0:
    k = int(input())
    count = 0
    for i in range(len(res)):
        if k == min(res[i]):
            count += 1
    print(count)
    q -= 1

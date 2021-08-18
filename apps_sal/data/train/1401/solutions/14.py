n, k = list(map(int, input().split()))
chpr = list(map(int, input().split()))
chpr.sort()
res = 0
for i in range(len(chpr)):
    if chpr[i] <= k:
        k = k - chpr[i]
        res = res + 1
    else:
        break
print(res)

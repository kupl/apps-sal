(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
sumi = 0
ans = 10 ** 20
for i in range(len(a)):
    sumi = sum(a)
    for j in range(i, len(a)):
        sumi = sumi - a[j] + a[j] / k
        ans = min(ans, sumi)
print(ans)

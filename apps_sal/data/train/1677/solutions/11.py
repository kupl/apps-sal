n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.insert(0, 0)
b.insert(0, 0)

prefixsum = [0 for _ in range(n+1)]
for i in range(1, n+1):
    prefixsum[i] = prefixsum[i-1] + b[i]

def ssum(i, j):
    if i < j:
        return a[i] + a[j] + prefixsum[j-1] - prefixsum[i]
    elif i > j:
        return a[i] + a[j] + prefixsum[n] - (prefixsum[i] - prefixsum[j-1])
    else:
        return a[i]

ans = float('-inf')
for i in range(1, n+1):
    for j in range(1, n+1):
        ans = max(ans, ssum(i, j))

print(ans)

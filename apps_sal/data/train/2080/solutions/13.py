m = int(input())
q = list(map(int, input().split()))
c = min(q)

n = int(input())
a = list(map(int, input().split()))
a.sort()

res = 0
for i in range(n):
    if i % (c + 2) < c:
        res += a[n - 1 - i]
print(res)

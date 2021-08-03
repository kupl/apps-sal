n = int(input())
a = [int(i) for i in input().split()]
d = {}
for i in a:
    d[i] = 0

for i in a:
    d[i] += 1

ans = n - max(d.values())
print(ans)

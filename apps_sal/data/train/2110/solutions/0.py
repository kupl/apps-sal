n = int(input())
a = [int(x) for x in input().split()]
l = [0] * (10**6 + 100)
for x in a:
	l[x] += 1
cur = 0
ans = 0
for x in l:
	cur += x
	if cur % 2:
		ans += 1
	cur //= 2
print(ans)


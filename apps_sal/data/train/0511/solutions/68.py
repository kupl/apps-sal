N = int(input())
lst = list(map(int, input().split()))
sx = lst[0]
for i in range(1, N):
	sx = sx^lst[i]
print(*[i^sx for i in lst])

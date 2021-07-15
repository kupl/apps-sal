n = int(input())
a = list(map(int, input().split()))

a.sort()

i = 0
for j in range(n):
	if a[i] < a[j]:
		i = i + 1

print(i)

n, k = [int(x) for x in input().split()]
ans = []
for i in range(k):
	if i % 2:
		ans.append(str(n - i // 2))
	else:
		ans.append(str(i // 2 + 1))
for i in range(n - k):
	if k % 2:
		ans.append(str(k // 2 + 2 + i))
	else:
		ans.append(str(n - k // 2 - i))
print(' '.join(ans))


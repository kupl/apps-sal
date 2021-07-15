X, D = list(map(int, input().split()))
cn = 1
add0 = 1 if (X&1) else 0
ans = []
for i in range(30,0,-1):
	if not (X & (1<<i)): continue
	ans += [cn]*i
	add0 += 1
	cn += D
for i in range(add0):
	ans.append(cn)
	cn += D
print(len(ans))
print(' '.join(map(str, ans)))


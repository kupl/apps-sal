n = int(input())
if n==1:
	print(0)
	return
elif n==2:
	print(1)
	print(2)
	return

ans = 0
pr = [0] * (n+1)
p = []
end = 1

while end > 0:
	i = 2
	while pr[i] != 0: 
		i += 1
		if i==n+1:
			end = 0
			break
	if i != n+1:
		pr[i] = 1
		p.append(i)
	j = i
	while i+j<=n: 
		i += j
		pr[i] = 2
res = []
for a in p:
	x = a
	while x <= n:
		res.append(x)
		ans += 1
		x *= a

print(ans)
print(*res)


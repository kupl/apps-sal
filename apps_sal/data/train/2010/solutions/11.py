def powmod(x, p, m):
	if p <= 0:
		return 1
	if p <= 1:
		return x%m
	return powmod(x*x%m, p//2, m) * (x%m)**(p%2) % m

###

n = int(input())
#print(n)
h = [0] + [int(x) for x in input().split()] + [0]
#print(h)

for i in range(1, len(h)):
	h[i] = min(h[i], h[i-1]+1)
	h[-i-1] = min(h[-i-1], h[-i]+1)

#print(h)
ans = max(h)
print(ans)





































































































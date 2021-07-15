n = int(input())
ans = ''
while n > 0:
	p, q, b = list(map(int, input().split(' ')))
	for i in range(6):
		b = b * b % q
	if b * p % q == 0: ans += 'Finite\n'
	else: ans += 'Infinite\n'
	n -= 1
print (ans)


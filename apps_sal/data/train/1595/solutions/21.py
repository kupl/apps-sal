def evaluate(a, b):
	ans = ''
	for i in range(0, len(a)):
		if a[i] == b[i]:
			ans += '-'
		else:
			ans += '+'
	return ans

def dp(p_bar, n, s):
	mod = 10**7 + 9
	if n == 0:
		return 0
	elif n == 1:
		k = 0
		if p_bar == s[0]:
			k += 1
		if p_bar == "----------":
			k += 1
		return k
	else:
		return (dp(p_bar, n-1, s)%mod + dp(evaluate(p_bar, s[n-1]), n-1, s))%mod


t = int(input())

for i in range(0, t):
	p = input()
	n = int(input())
	s = []
	for j in range(0, n):
		temp = input()
		s.append(temp)
	p_bar = ''
	for j in p:
		if j == 'w':
			p_bar += '+'
		else:
			p_bar += '-'
	print(dp(p_bar, n, s))

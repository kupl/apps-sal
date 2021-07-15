def SieveOfEratosthenes(n): 
	prime = [True for i in range(n+1)] ; ans = [];p = 2
	while (p * p <= n): 
		if (prime[p] == True): 
			for i in range(p * p, n+1, p):prime[i] = False
		p += 1
	for p in range(2, n+1): 
		if prime[p]:ans.append(p) 
	return ans
p = SieveOfEratosthenes(10**6+10)
for _ in range(int(input())):
	n = int(input());s = 0
	for i in range(len(p)):
		if p[i] > n:break
		else:s += p[i]
	print(s%10)

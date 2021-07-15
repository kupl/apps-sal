def primalsum(n): 
	prime = [True] * (n + 1);p = 2;sum_ = 0
	while(p**2 <= n):
		if(prime[p] == True):
			i = p*2
			while(i <= n): prime[i] = False;i += p
		p += 1
	for i in range (2,n + 1): 
		if(prime[i]): sum_ += i 
	return sum_
for _ in range(int(input())):N = int(input());print(str(primalsum(N))[-1]) 

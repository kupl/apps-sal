def primes(n):
	primes, p = [True for i in range(n+1)], 2

	while p**2 <= n:
		if primes[p]:
			for i in range(p*2, n+1, p): primes[i] = False
		p += 1
	primes[0], primes[1] = False, False

	return ''.join([str(i) for i in range(n+1) if primes[i]])


def solve(a, b):
	re = primes(a*10)
	return re[a:b+a]

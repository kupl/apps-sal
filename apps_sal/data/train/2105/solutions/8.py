import math

def eratosthenes(n):
	is_composite = [False for _ in range(n+1)]
	is_composite[0] = is_composite[1] = True

	b = math.floor(math.sqrt(n)) + 1

	for p in range(2, b+1):
		if is_composite[p]:
			continue

		x = 2*p
		while x <= n:
			is_composite[x] = True
			x += p

	return is_composite
	#return [k for k in range(2, n+1) if not is_composite[k]]

n = int(input())
is_composite = eratosthenes(n+1)

if n >= 3:
	print(2)
else:
	print(1)

print(*(1 if not is_composite[k] else 2 for k in range(2, n+2)))




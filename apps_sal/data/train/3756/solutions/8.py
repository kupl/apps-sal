sieve = [False] * 2 + [True] * 32000
for i in range(2, 200):
    if sieve[i]:
        for j in range(2, 32000):
            if i * j >= len(sieve): break
            sieve[i*j] = False

def goldbach_partitions(n):
    if n % 2: return []
    if n == 4: return ['2+2']
    return ['{}+{}'.format(i, n-i) for i in range(2, n//2+1) if sieve[i] and sieve[n-i]]

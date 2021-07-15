primes = [3]
primes_set = {2, 3}
dominant = [3]

for n in range(5, 500000, 2):
    for p in primes:
        if p*p > n:
            primes.append(n)
            primes_set.add(n)
            if len(primes_set) in primes_set:
                dominant.append(n)
            break
        if n%p == 0:
            break

def solve(a, b):
    return sum(p for p in dominant if a <= p <= b)

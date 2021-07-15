odd_primes = {n for n in range(3, 32000, 2) if all(n % k for k in range(3, int(n**0.5)+1, 2))}

def goldbach_partitions(n):
    if n % 2 == 1:
        return []
    if n == 4:
        return ["2+2"]
    return [f"{p}+{q}" for p, q in sorted((p, n-p) for p in odd_primes if p <= (n-p) and (n-p) in odd_primes)]


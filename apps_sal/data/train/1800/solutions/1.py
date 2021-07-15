from collections import defaultdict

# generate list of primes
SIEVE_LIMIT = 10**5
sieve = list(range(SIEVE_LIMIT))
sieve[1] = 0
# and store them based on used digits
cache = defaultdict(list)
for n in sieve:
    if n:
        digits = tuple(sorted(str(n)))
        cache[digits].append(n)
        for i in range(n*n, SIEVE_LIMIT, n):
            sieve[i] = 0


# return the number of items in arr below given limit
def items_below_limit(arr, limit):
    return sum( [x < limit for x in arr] )


# return number of primes with given permutations below limit
def find_prime_kPerm(limit, perms):
    res = []
    for k, v in list(cache.items()):
        if  items_below_limit(v, limit) == perms + 1:
            res.append(v[0])
    
    return [ len(res), min(res), max(res) ] if res else [0, 0, 0]


from random import randint

def squares(n):
    return [pow(i, 2) for i in range(1, n + 1)]

def num_range(n, start, step):
    return list(range(start, start + n * step, step))

def rand_range(n, mn, mx):
    return [randint(mn, mx) for _ in range(n)]

def primes(n):
    return gen_primes(n)

def gen_primes(size):
    
    def nats(n):
        yield n
        yield from nats(n + 1)
    
    def sieve(gen):
        n = next(gen)
        yield n 
        yield from sieve(i for i in gen if i % n != 0)
    
    prime_gen = sieve(nats(2))
    return [next(prime_gen) for _ in range(size)]

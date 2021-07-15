# Can someone tell me if __import__ will be called each time in this case?
hotpo = __import__("functools").lru_cache(maxsize=None)(lambda n: 0 if n == 1 else 1+hotpo(3*n+1 if n&1 else n>>1))

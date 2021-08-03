ok = {i for i in range(22, 7778)
      if set(str(i)) <= set('2357')
      and not all(i % d for d in range(2, i))}


def not_primes(*a):
    return sorted(set(range(*a)) & ok)

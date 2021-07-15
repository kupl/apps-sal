from itertools import islice, count

#Python cookbook
def eratosthenes():
    D = {}
    yield 2
    for q in islice(count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p

def find_prime_kPerm(n, kPerm):
    d = {}
    for p in eratosthenes():
        if p > n: break
        k = ''.join(sorted(c for c in str(p)))
        d[k] = d.get(k, []) + [p]

    r = [min(v) for v in d.values() if len(v) == kPerm+1]
    return [len(r), min(r) if r else 0, max(r) if r else 0]    

import collections

def solve(a,b):
    d = collections.defaultdict(list)
    for n in range(a, b):
        d[(sum(k + n//k for k in range(1, int(n**0.5)+1) if n%k==0) - (int(n**0.5) if int(n**0.5) == n**0.5 else 0))/n].append(n)
    return sum(v[0] for v in list(d.values()) if len(v) > 1)


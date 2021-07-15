from functools import reduce; gcd=lambda a,b: gcd(b,a%b) if b else a; lcm=lambda a,b: a/gcd(a,b)*b; parameter=lambda n: (lambda n: lcm(sum(n),reduce(lambda a,b: a*b,n,1)))([int(e) for e in str(n)])

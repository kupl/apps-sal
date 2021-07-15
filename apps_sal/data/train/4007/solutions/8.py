from functools import reduce; gcd=lambda a,b: gcd(b,a%b) if b else a; finding_k=lambda arr: reduce(lambda a,b: gcd(a,b), [abs(e-arr[0]) for e in arr]) or -1

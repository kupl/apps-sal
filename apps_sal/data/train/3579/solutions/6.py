from math import factorial as f
choose=lambda n,k:f(n)/(f(k)*f(n-k)) if k <= n else 0
